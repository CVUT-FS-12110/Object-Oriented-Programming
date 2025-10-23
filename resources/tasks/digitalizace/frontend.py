import streamlit as st
import pandas as pd
import os
import uuid # Pro generování unikátních ID
from passlib.hash import pbkdf2_sha256 # Pro bezpečné hashování hesel

# --- KROK 1: Import logiky od studentů ---
try:
    from backend import Stavebnik, Urednik, Zadost, StavebniUrad, Osoba
except ImportError:
    st.error("CHYBA: Nenašel jsem soubor 'backend.py' nebo v něm chybí potřebné třídy!")
    st.error("Ujistěte se, že máte 'backend.py' ve stejné složce.")
    st.stop() 

# --- KROK 2: Definice CSV souborů ---
UZIVATELE_CSV = 'uzivatele.csv'
ZADOSTI_CSV = 'zadosti.csv'

# --- KROK 3: Funkce pro práci s databází (CSV) ---

def inicializuj_databaze():
    """
    Pokud neexistují CSV soubory, vytvoří je i s ukázkovými daty.
    """
    if not os.path.exists(UZIVATELE_CSV):
        print("INFO: Vytvářím 'uzivatele.csv' s defaultními hesly 'heslo123'...")
        heslo_urednika = pbkdf2_sha256.hash("heslo123")
        heslo_stav1 = pbkdf2_sha256.hash("heslo123")
        heslo_stav2 = pbkdf2_sha256.hash("heslo123")
        
        data = [
            {'id_uzivatele': 'u001', 'jmeno': 'Pavel Přísný', 'email': 'pavel@urad.gov', 'role': 'urednik', 'detail_role': 'A-102', 'heslo_hash': heslo_urednika},
            {'id_uzivatele': 's001', 'jmeno': 'Karel Nový', 'email': 'karel@email.cz', 'role': 'stavebnik', 'detail_role': '123456789', 'heslo_hash': heslo_stav1},
            {'id_uzivatele': 's002', 'jmeno': 'Jana Pilná', 'email': 'jana@email.cz', 'role': 'stavebnik', 'detail_role': '987654321', 'heslo_hash': heslo_stav2},
        ]
        df = pd.DataFrame(data)
        df.to_csv(UZIVATELE_CSV, index=False)
        
    if not os.path.exists(ZADOSTI_CSV):
        print("INFO: Vytvářím prázdný 'zadosti.csv'...")
        df = pd.DataFrame(columns=['id_zadosti', 'adresa_stavby', 'stav', 'id_stavebnika', 'id_urednika'])
        df.to_csv(ZADOSTI_CSV, index=False)

def nacti_vsechna_data():
    """
    Hlavní "hydratační" funkce.
    OPRAVA: Používáme dtype=str, aby pandas nenahrazoval stringy za floaty.
    """
    print("INFO: Načítám data z CSV a vytvářím objekty...")
    
    uzivatele_mapa = {}
    uzivatele_db_data = {} 
    
    # --- OPRAVA ZDE ---
    # Donutíme pandas číst VŠECHNY sloupce jako string, aby se zabránilo chybě s float
    df_uziv = pd.read_csv(UZIVATELE_CSV, dtype=str).fillna('')
    
    for _, radek in df_uziv.iterrows():
        uzivatele_db_data[radek['email']] = radek.to_dict()
        
        if radek['role'] == 'urednik':
            obj = Urednik(jmeno=radek['jmeno'], email=radek['email'], 
                          kancelar=radek['detail_role'], id_osoby=radek['id_uzivatele'])
        elif radek['role'] == 'stavebnik':
            obj = Stavebnik(jmeno=radek['jmeno'], email=radek['email'], 
                            telefon=radek['detail_role'], id_osoby=radek['id_uzivatele'])
        uzivatele_mapa[radek['id_uzivatele']] = obj

    urad = StavebniUrad()
    if os.path.exists(ZADOSTI_CSV) and os.path.getsize(ZADOSTI_CSV) > 0:
        
        # --- OPRAVA ZDE ---
        # Také zde donutíme číst vše jako string a vyplníme prázdné buňky
        df_zad = pd.read_csv(ZADOSTI_CSV, dtype=str).fillna('') 
        
        for _, radek in df_zad.iterrows():
            stavebnik_obj = uzivatele_mapa.get(radek['id_stavebnika'])
            urednik_obj = uzivatele_mapa.get(radek['id_urednika']) # Teď už je to bezpečné
            
            if not stavebnik_obj:
                print(f"WARN: Stavebník '{radek['id_stavebnika']}' nenalezen. Přeskakuji žádost.")
                continue
                
            zadost = Zadost(stavebnik_obj=stavebnik_obj, 
                              adresa_stavby=radek['adresa_stavby'], 
                              id_zadosti=radek['id_zadosti'])
            
            zadost._stav = radek['stav']
            if urednik_obj:
                zadost._prirazeny_urednik = urednik_obj
            urad.podat_zadost(zadost)
            
    return urad, uzivatele_mapa, uzivatele_db_data

def uloz_zadosti_do_csv(urad_obj):
    """
    Uloží změny v žádostech zpět do CSV.
    """
    print("INFO: Ukládám změny do 'zadosti.csv'...")
    data = []
    for zadost in urad_obj._databaze_zadosti:
        data.append({
            'id_zadosti': zadost.id_zadosti,
            'adresa_stavby': zadost.adresa_stavby,
            'stav': zadost._stav,
            'id_stavebnika': zadost.stavebnik_obj.id_osoby,
            'id_urednika': zadost._prirazeny_urednik.id_osoby if zadost._prirazeny_urednik else None
        })
    
    # Při ukládání nahradíme None za prázdný string pro konzistenci
    df = pd.DataFrame(data).fillna('')
    df.to_csv(ZADOSTI_CSV, index=False)


# --- KROK 4: Inicializace aplikace ---

inicializuj_databaze()

# Načteme všechna data do st.session_state (spustí se jen jednou)
if 'app_initialized' not in st.session_state:
    try:
        urad_obj, uzivatele_mapa_obj, uziv_db_data_obj = nacti_vsechna_data()
        st.session_state['urad'] = urad_obj
        st.session_state['uzivatele_mapa'] = uzivatele_mapa_obj # Mapa ID -> Objekt
        st.session_state['uzivatele_db'] = uziv_db_data_obj   # Mapa Email -> Řádek CSV (pro login)
        st.session_state['app_initialized'] = True
    except Exception as e:
        st.error(f"Došlo k chybě při načítání databáze: {e}")
        st.error("Zkuste smazat soubory 'uzivatele.csv' a 'zadosti.csv' a restartovat aplikaci.")
        st.stop()


# Získáme odkazy na naše živé objekty ze session state
urad = st.session_state['urad']
uzivatele_mapa = st.session_state['uzivatele_mapa']
uzivatele_db = st.session_state['uzivatele_db']


# --- KROK 5: Logika Přihlášení / Registrace / Odhlášení ---

st.sidebar.title("Portál eStavba 1.0")

if 'prihlaseny_uzivatel_id' not in st.session_state:
    
    mod = st.sidebar.radio("Vyberte akci:", ["Přihlásit se", "Registrovat se"])
    st.title(mod)
    st.markdown("---")

    # --- Formulář pro PŘIHLÁŠENÍ ---
    if mod == "Přihlásit se":
        with st.form("login_form"):
            email = st.text_input("Email (např. 'karel@email.cz')")
            heslo = st.text_input("Heslo (defaultně 'heslo123')", type="password")
            submit = st.form_submit_button("Přihlásit")
            
            if submit:
                user_data = uzivatele_db.get(email)
                
                if not user_data:
                    st.error("Uživatel s tímto emailem neexistuje.")
                else:
                    ulozeny_hash = user_data['heslo_hash']
                    
                    # Ověříme, že hash je string (díky dtype=str by měl být)
                    if not isinstance(ulozeny_hash, str) or not ulozeny_hash:
                        st.error("Chyba databáze: Hash hesla není platný. Kontaktujte admina.")
                    elif pbkdf2_sha256.verify(heslo, ulozeny_hash):
                        st.success("Přihlášení úspěšné!")
                        st.session_state['prihlaseny_uzivatel_id'] = user_data['id_uzivatele']
                        st.rerun()
                    else:
                        st.error("Špatné heslo.")

    # --- Formulář pro REGISTRACI ---
    elif mod == "Registrovat se":
        st.info("Úředníky může zakládat pouze administrátor. Registrace je jen pro stavebníky.")
        
        with st.form("registracni_form"):
            jmeno = st.text_input("Celé jméno")
            email = st.text_input("Kontaktní email")
            telefon = st.text_input("Telefonní číslo")
            heslo = st.text_input("Heslo", type="password")
            potvrzeni_hesla = st.text_input("Potvrzení hesla", type="password")
            submit_button = st.form_submit_button("Zaregistrovat se")
            
            if submit_button:
                if not jmeno or not email or not telefon or not heslo:
                    st.error("Musíte vyplnit všechna pole!")
                elif heslo != potvrzeni_hesla:
                    st.error("Hesla se neshodují!")
                elif email in uzivatele_db:
                    st.error("Uživatel s tímto emailem již existuje!")
                else:
                    novy_id = f"s{uuid.uuid4().hex[:6]}"
                    novy_hash = pbkdf2_sha256.hash(heslo) 
                    
                    novy_uzivatel_data = {
                        'id_uzivatele': novy_id, 'jmeno': jmeno, 'email': email,
                        'role': 'stavebnik', 'detail_role': telefon, 'heslo_hash': novy_hash
                    }
                    
                    df_uziv = pd.read_csv(UZIVATELE_CSV, dtype=str).fillna('')
                    df_novy = pd.DataFrame([novy_uzivatel_data])
                    df_final = pd.concat([df_uziv, df_novy], ignore_index=True)
                    df_final.to_csv(UZIVATELE_CSV, index=False)
                    
                    st.success("Registrace proběhla úspěšně!")
                    st.info("Obnovuji aplikaci, nyní se můžete přihlásit.")
                    
                    del st.session_state['app_initialized']
                    st.rerun()

# --- KROK 6: Hlavní aplikace (pokud je uživatel přihlášen) ---
else:
    # Uživatel JE přihlášen. Získáme jeho "živý" OOP objekt.
    ja_id = st.session_state['prihlaseny_uzivatel_id']
    ja = uzivatele_mapa.get(ja_id) 
    
    if ja is None:
        # Pojistka, kdyby se něco pokazilo
        st.error("Došlo k chybě při načítání uživatele. Zkuste se odhlásit a přihlásit.")
        if st.sidebar.button("Nouzové odhlášení"):
            del st.session_state['prihlaseny_uzivatel_id']
            st.rerun()
        st.stop()


    st.sidebar.subheader(f"Přihlášen: {ja.jmeno}")
    with st.sidebar.expander("Zobrazit mé detaily"):
        if isinstance(ja, Stavebnik):
            st.write(f"Role: Stavebník")
            st.write(f"Email: {ja.email}")
            st.write(f"Telefon: {ja.telefon}")
        elif isinstance(ja, Urednik):
            st.write(f"Role: Úředník")
            st.write(f"Email: {ja.email}")
            st.write(f"Kancelář: {ja.kancelar}")
    
    if st.sidebar.button("Odhlásit se"):
        del st.session_state['prihlaseny_uzivatel_id']
        st.rerun()

    st.title(f"Vítejte v systému eStavba, {ja.jmeno}!")
    st.markdown("---")

    # --- Rozhraní pro ÚŘEDNÍKA ---
    if isinstance(ja, Urednik):
        st.header("Seznam žádostí k vyřízení")
        
        if not urad._databaze_zadosti:
            st.success("Všechny žádosti jsou vyřízené! 🥳")

        for zadost in urad._databaze_zadosti:
            st.subheader(f"Žádost: {zadost.id_zadosti} (Stav: `{zadost._stav}`)")
            with st.container(border=True):
                col1, col2 = st.columns(2)
                col1.write(f"**Adresa:** {zadost.adresa_stavby}")
                col1.write(f"**Stavebník:** {zadost.stavebnik_obj.jmeno} ({zadost.stavebnik_obj.email})")
                
                if zadost._prirazeny_urednik:
                    col2.write(f"**Vyřizuje:** {zadost._prirazeny_urednik.jmeno}")
                else:
                    col2.write(f"**Vyřizuje:** (Zatím nepřiřazeno)")

                if zadost._stav == "Podáno":
                    if st.button("Přiřadit mně", key=f"prirad_{zadost.id_zadosti}"):
                        zadost.prirad_urednika(ja) 
                        uloz_zadosti_do_csv(urad)  
                        st.rerun()

                elif zadost._stav == "V řízení":
                    if zadost._prirazeny_urednik == ja:
                        if st.button("✅ Schválit", key=f"schval_{zadost.id_zadosti}"):
                            zadost.zmen_stav("Schváleno") 
                            uloz_zadosti_do_csv(urad)     
                            st.rerun()
                        if st.button("❌ Zamítnout", key=f"zamit_{zadost.id_zadosti}"):
                            zadost.zmen_stav("Zamítnuto") 
                            uloz_zadosti_do_csv(urad)    
                            st.rerun()
                    else:
                        st.warning("Tuto žádost vyřizuje jiný úředník.")

    # --- Rozhraní pro STAVEBNÍKA ---
    elif isinstance(ja, Stavebnik):
        st.header("Podat novou žádost")
        with st.form("nova_zadost_form"):
            adresa = st.text_input("Adresa plánované stavby:")
            podat_tlacitko = st.form_submit_button("Podat žádost")
            
            if podat_tlacitko and adresa:
                novy_id = f"z{uuid.uuid4().hex[:4]}" 
                nova_zadost = Zadost(stavebnik_obj=ja, 
                                       adresa_stavby=adresa, 
                                       id_zadosti=novy_id)
                urad.podat_zadost(nova_zadost)
                uloz_zadosti_do_csv(urad)
                st.success(f"Žádost {novy_id} byla úspěšně podána!")

        st.markdown("---")
        st.header("Stav mých podaných žádostí")
        
        moje_zadosti = [z for z in urad._databaze_zadosti if z.stavebnik_obj == ja]
        
        if not moje_zadosti:
            st.info("Zatím jste nepodal žádnou žádost.")
            
        for zadost in moje_zadosti:
            if zadost._stav == "Schváleno":
                st.success(f"**{zadost.adresa_stavby}** | Stav: {zadost._stav}")
            elif zadost._stav == "Zamítnuto":
                st.error(f"**{zadost.adresa_stavby}** | Stav: {zadost._stav}")
            else:
                st.info(f"**{zadost.adresa_stavby}** | Stav: {zadost._stav}")
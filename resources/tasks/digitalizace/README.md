# Digitalizace stavebního řízení
Vaším úkolem je implementovat třídy v souboru [backend.py](backend.py) tak aby fungovalo spuštění [frontend.py](frontend.py).

## Spuštění aplikace
Nejprve musíte nainstalovat package pro tvorbu webových aplikací Streamlit:
```bash
pip install streamlit
```
Poté spusťte frontend.py
```bash
streamlit run frontend.py
```

## Popis úkolu

Implementujte objektově orientovaný systém pro digitalizaci stavebního řízení. Systém simuluje proces podávání a vyřizování žádostí o stavební povolení mezi stavebníky a úředníky.

**Vaším úkolem je:**
1. Prostudovat kód v `frontend.py` a zjistit, jaké třídy, atributy a metody jsou očekávány
2. Implementovat všechny potřebné třídy v `backend.py` s kompletní funkčností
3. Implementovat správné chování pro stavy žádostí a jejich změny

## Popis tříd

Systém obsahuje třídy `Osoba`, `Stavebnik`, `Urednik`, `Zadost` a `StavebniUrad` pro správu celého systému.

**Tip:** Pečlivě si prohlédněte, jak jsou objekty vytvářeny a používány ve `frontend.py`. Všímejte si zejména konstruktorů, přístupu k atributům a volání metod.

## Testování funkčnosti

Úspěšná implementace umožní:
- Přihlášení jako úředník (pavel@urad.gov, heslo: heslo123)  
- Přihlášení jako stavebník (karel@email.cz, heslo: heslo123)
- Registraci nového stavebníka
- Podávání žádostí stavebníky
- Přiřazování a vyřizování žádostí úředníky
- Sledování stavu žádostí

Pokud se frontend spustí bez chyb a všechny funkce fungují, máte hotovo!

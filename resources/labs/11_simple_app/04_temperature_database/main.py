import fastapi
import uvicorn
import sqlite3

DATABASE_FILE = "example.db"
app = fastapi.FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/temperature")
def post_temperature(temperature: float):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO temperature VALUES (NULL, {temperature})")
    conn.commit()
    return {"status": "ok"}


@app.get("/temperature")
def get_last_temperature():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    res = cursor.execute("SELECT * FROM temperature ORDER BY id DESC LIMIT 1")
    return {"temperature": res.fetchone()}


@app.get("/temperature_list")
def get_temperature_list():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    res = cursor.execute("SELECT * FROM temperature")
    return {"temperature": res.fetchall()}


if __name__ == "__main__":
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS temperature(id integer primary key autoincrement, value)''')
    conn.commit()
    conn.close()

    uvicorn.run("main:app", reload=True)

import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/temperature")
def post_temperature(temperature: float):
    with open("temperature.txt", "a") as file:
        file.write(f"{temperature}\n")

    return {"status": "ok"}


@app.get("/temperature")
def get_last_temperature():
    with open("temperature.txt") as file:
        content = file.readlines()

    return {"temperature": float(content[-1].strip())}


if __name__ == "__main__":
    uvicorn.run(app)

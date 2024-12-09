import fastapi
import uvicorn
import datetime


app = fastapi.FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/temperature")
def post_temperature(temperature: float):
    timestamp = datetime.datetime.now()
    with open("temperature.txt", "a") as file:
        file.write(f"{timestamp};{temperature}\n")

    return {"status": "ok"}


@app.get("/temperature")
def get_last_temperature():
    with open("temperature.txt") as file:
        content = file.readlines()

    timestamp, temperature = content[-1].strip().split(";")
    ret = {
        "timestamp": timestamp,
        "temperature": float(temperature),
    }
    return ret

@app.get("/temperature_list")
def get_temperature_list():
    with open("temperature.txt") as file:
        content = file.readlines()

    ret = []
    for line in content:
        timestamp, temperature = line.strip().split(";")
        ret.append({
            "timestamp": timestamp,
            "temperature": float(temperature),
        })
    return ret


if __name__ == "__main__":
    uvicorn.run(app)

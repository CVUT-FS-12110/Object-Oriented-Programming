import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

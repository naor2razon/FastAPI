
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def example():
    return {"FastAPI": "The web framework!"}


@app.get("/greetings")
def greeting():
    return {"Hello REST API!"}


@app.get("/names")
def greeting():
    return {"name1": "naor", "name2": "razon", "name3": "on"}


if __name__ == "__main__":
    uvicorn.run("main:app")
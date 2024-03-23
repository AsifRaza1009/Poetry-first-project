from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"My first api call in fast api  "}

@app.get("/city")
def city():
    return { " City ": "Sahiwal is my city"}
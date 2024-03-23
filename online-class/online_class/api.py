from fastapi import FastAPI

new= FastAPI()

@new.get("/")
def read_root():
    return {"this is my second attempt to FastApi call"}

@new.get("/method")
def read_root():
    return {"Method": " Python Fast Api method is used for this class"}

@new.get('/work')
def work():
    return{"work": " I work in city of sahiwal "}
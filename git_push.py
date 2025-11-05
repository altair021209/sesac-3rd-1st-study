from fastapi import FastAPI

app=FastAPI()
@app.get("/ping")
def index():
    msg = "pong"
    return {"msg": msg}
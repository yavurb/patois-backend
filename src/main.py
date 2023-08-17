from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome() -> dict:
  return { "message": "Hello World" }
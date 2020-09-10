from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="static", check_dir=True, html=True), name="static")


@app.get("/api")
async def root():
    return {"message": "Hello World"}

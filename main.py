from fastapi import FastAPI
from fastapi.responses import FileResponse
from jobs import get_jobs

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/api/jobs")
def jobs():
    return get_jobs()

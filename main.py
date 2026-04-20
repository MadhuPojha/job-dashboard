from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jobs import get_jobs, refresh_jobs

app = FastAPI()


# API (FAST - uses CACHE)
@app.get("/api/jobs")
def jobs_api():
    return get_jobs()


# MANUAL REFRESH (optional)
@app.get("/api/refresh")
def refresh():
    return {"status": "refreshing", "jobs": refresh_jobs()}


# FRONTEND
@app.get("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())
from fastapi import FastAPI

from app.routers import links, redirect

app = FastAPI(title="Encurtador de URL")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/version")
def version():
    return {"version": "0.1.0"}

app.include_router(links.router)
app.include_router(redirect.router)
from fastapi import FastAPI

app = FastAPI(title="Encurtador de URL")

@app.get("/health")
def health():
    return {"status": "ok"}

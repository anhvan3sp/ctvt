from fastapi import FastAPI
from modules import auth

app = FastAPI(title="CTVT2 API", version="1.0")

@app.get("/")
def root():
    return {"status": "CTVT2 API running"}

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

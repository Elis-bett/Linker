from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.session import SessionLocal
from services.link_service import shortenUrl

app = FastAPI(title="Linker")

@app.post("/short")
def short_url(smth):
    return {"original url": smth}


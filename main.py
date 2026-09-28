from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.session import SessionLocal
from services.link_service import shortenUrl, getOriginalUrl
from datetime import datetime, timedelta

app = FastAPI(title="Linker")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/short")
async def short_url(url: str, db: Session = Depends(get_db)):
    result = shortenUrl(url) # получаем из сервиса короткую запись 
    return {
        "short": f"http://localhost:8000/{result['short_code']}",
        "original": url,
        "created": datetime.now(), #TODO:  нормально время создания, то же что и в бд записывается
        "expires": datetime.now() + timedelta(days=5)
    }


# перекидываем на исходную ссылку по короткой
@app.get("/{short}")
async def redirect_url(shortUrl: str, db: Session = Depends(get_db)):
    originalUrl = getOriginalUrl(db, shortUrl)
    #TODO: обработать случай когда не нашли ссылку в бд
    return {RedirectResponse(url=originalUrl, status_code=302)}

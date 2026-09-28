from database.models import Links
import hashlib
from datetime import datetime, timedelta
#from database.session import SessionLocal
from sqlalchemy.orm import Session

def getStringFromHash(hash) -> str:
    res = ""
    j = 0
    for i in range(len(hash)//3):
        res += str(int(hash[j:j+3], 16) % 64)
        j += 3
    return res


def saveUrl(db: Session, url: str):
    short = shortenUrl(url)
    # TODO: CHECK IF THE SHORTENED URL IS UNIQUE (возможно это надо будет в main все-таки реализовать)
    newLink = Links(url=url, short=short, created=datetime.now(), expired=datetime.now()+timedelta(days=5)) # MAGIC NUMBER потом убрать эту пятерку и сделать корректнее
    db.add(newLink) #добавили
    db.commit() #закоммитили
    db.refresh(newLink) #сохранили в бд

    return {
        "original": url,
        "short": short
            }

# The function return shortened code for the given url
def shortenUrl(url) -> str:
    sha256 = hashlib.sha256()
    sha256.update(url)
    url_hash = sha256.hexdigest()
    result = getStringFromHash(url_hash)
    return result


    
def getOriginalUrl(db: Session, short: str) -> str:
    result = db.query(Links).filter(Links.short == short).first()
    #TODO: обработать если не нашли ссылку
    #TODO: обработать проверку что ссылка не просрочилась (надо еще как-то удаление реализовать)
    return result
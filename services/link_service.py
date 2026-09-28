from database.models import Links
from hashlib import sha256
from datetime import datetime, timedelta

def getStringFromHash(hash) -> str:
    res = ""
    j = 0
    for i in range(len(hash)//3):
        res += str(int(hash[j:j+3], 16) % 64)
        j += 3
    return res

# The function return shortened code for the given url
def shortenUrl(url) -> str:
    sha256 = sha256()
    sha256.update(url)
    url_hash = sha256.hexdigest()
    result = getStringFromHash(url_hash)
    return result


# TODO: CHECK IF THE SHORTENED URL IS UNIQUE


def link(url) -> str:
    newUrl = shortenUrl(url)

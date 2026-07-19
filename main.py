from fastapi import FastAPI

app = FastAPI()

@app.post("/short")
def short_url(smth):
    return {"original url": smth}


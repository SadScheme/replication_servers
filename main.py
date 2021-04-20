from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    with open("./html/index.html") as index123:
        html = index123.read()

    return HTMLResponse(content=html, status_code=200)
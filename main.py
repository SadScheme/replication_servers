from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
import shutil


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    with open("./html/index.html") as index123:
        html = index123.read()
    return HTMLResponse(content=html, status_code=200)


@app.post("/post", response_class=HTMLResponse)
async def upload1(sentdata: UploadFile = File(...)):
    with open(f"{sentdata.filename}", "wb") as buffer:
        shutil.copyfileobj(sentdata.file, buffer)
    return {"filename": sentdata.filename}


@app.post("/post1")
async def upload(request: Request):
    da = await request.body()
    print(da)
    da1 = jsonable_encoder(da)
    return da1

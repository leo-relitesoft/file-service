from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "File service"}

@app.get("/upload")
async def upload():
    return {"upload": "ok"}

@app.get("/download")
async def download():
    return {"download": "ok"}

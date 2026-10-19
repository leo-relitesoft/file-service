import uvicorn
from fastapi import FastAPI, UploadFile, Path

app = FastAPI()


@app.get("/{file:path}")
async def read_file(file: str):
    return {"path": file}

@app.get("/upload")
async def upload():
    return {"upload": "ok"}

@app.get("/download")
async def download():
    return {"download": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8333)
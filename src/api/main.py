from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path
from src.api.predict import process_image

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("public/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_path = Path(f"public/{file.filename}")
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    enhanced_image_path = process_image(file_path)
    
    return FileResponse(enhanced_image_path)

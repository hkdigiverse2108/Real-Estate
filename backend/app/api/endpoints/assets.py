from fastapi import APIRouter, HTTPException, UploadFile, File
import os
import shutil
import re
from typing import List

router = APIRouter()

# Path to the frontend public assets folder relative to the backend app root
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "../../../../frontend/public/assets")

def sanitize_filename(filename: str) -> str:
    # Remove special characters and replace spaces with dashes
    name, ext = os.path.splitext(filename)
    clean_name = re.sub(r'[^a-zA-Z0-9]', '-', name).lower()
    clean_name = re.sub(r'-+', '-', clean_name).strip('-')
    return f"{clean_name}{ext.lower()}"

@router.get("/", response_model=List[str])
async def list_assets():
    if not os.path.exists(ASSETS_DIR):
        print(f"ERROR: Assets directory not found at {ASSETS_DIR}")
        return []
        
    try:
        files = [
            f for f in os.listdir(ASSETS_DIR) 
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'))
        ]
        return [f"/assets/{f}" for f in files]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload")
async def upload_asset(file: UploadFile = File(...)):
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR, exist_ok=True)
        
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")
        
    base_name = sanitize_filename(file.filename)
    filename = base_name
    
    # Ensure unique filename
    counter = 1
    name, ext = os.path.splitext(base_name)
    while os.path.exists(os.path.join(ASSETS_DIR, filename)):
        filename = f"{name}-{counter}{ext}"
        counter += 1
        
    file_path = os.path.join(ASSETS_DIR, filename)
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": filename, "path": f"/assets/{filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")

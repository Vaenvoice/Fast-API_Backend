from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.get("/")
async def get_images():
    """Get all images"""
    return {"message": "Images endpoint", "data": []}

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """Upload an image"""
    return {"message": "Image uploaded", "filename": file.filename}

@router.get("/{image_id}")
async def get_image(image_id: int):
    """Get a specific image"""
    return {"message": f"Image {image_id}", "id": image_id}

@router.delete("/{image_id}")
async def delete_image(image_id: int):
    """Delete an image"""
    return {"message": f"Image {image_id} deleted", "id": image_id}
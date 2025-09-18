from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Image
from schemas import ImageCreate, ImageResponse

router = APIRouter()

# GET /images - list all images
@router.get("/", response_model=List[ImageResponse])
def get_images(db: Session = Depends(get_db)):
    return db.query(Image).all()

# GET /images/{id} - get single image metadata
@router.get("/{id}", response_model=ImageResponse)
def get_image(id: int, db: Session = Depends(get_db)):
    image = db.query(Image).filter(Image.id == id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    return image

# POST /images - add new image
@router.post("/", response_model=ImageResponse)
def create_image(image: ImageCreate, db: Session = Depends(get_db)):
    db_image = Image(**image.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# DELETE /images/{id} - delete image
@router.delete("/{id}")
def delete_image(id: int, db: Session = Depends(get_db)):
    image = db.query(Image).filter(Image.id == id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    db.delete(image)
    db.commit()
    return {"detail": "Image deleted successfully"}

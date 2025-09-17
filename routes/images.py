from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Image
from schemas import ImageCreate, ImageResponse

router = APIRouter()


@router.get("/", response_model=List[ImageResponse])
async def get_images(db: Session = Depends(get_db)):
    """Get all images"""
    images = db.query(Image).all()
    return images


@router.post("/", response_model=ImageResponse)
async def create_image(image: ImageCreate, db: Session = Depends(get_db)):
    """Add new image"""
    db_image = Image(**image.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
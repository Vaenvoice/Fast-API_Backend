import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Image
from schemas import ImageCreate, ImageResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/", response_model=List[ImageResponse])
def get_images(db: Session = Depends(get_db)):
    logger.info("Fetching all images")
    return db.query(Image).all()

@router.get("/{id}", response_model=ImageResponse)
def get_image(id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching image with id={id}")
    image = db.query(Image).filter(Image.id == id).first()
    if not image:
        logger.warning(f"Image id={id} not found")
        raise HTTPException(status_code=404, detail="Image not found")
    return image

@router.post("/", response_model=ImageResponse)
def create_image(image: ImageCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating new image: {image.title}")
    db_image = Image(**image.model_dump())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

@router.delete("/{id}")
def delete_image(id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting image id={id}")
    image = db.query(Image).filter(Image.id == id).first()
    if not image:
        logger.warning(f"Image id={id} not found for delete")
        raise HTTPException(status_code=404, detail="Image not found")
    db.delete(image)
    db.commit()
    return {"detail": "Image deleted successfully"}

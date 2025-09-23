import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Annotation, Image
from schemas import AnnotationCreate, AnnotationResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=AnnotationResponse)
async def create_annotation(annotation: AnnotationCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating annotation for image_id={annotation.image_id}")
    image = db.query(Image).filter(Image.id == annotation.image_id).first()
    if not image:
        logger.warning(f"Image id={annotation.image_id} not found for annotation")
        raise HTTPException(status_code=404, detail="Image not found")
    db_annotation = Annotation(**annotation.model_dump())
    db.add(db_annotation)
    db.commit()
    db.refresh(db_annotation)
    return db_annotation

@router.get("/{image_id}", response_model=List[AnnotationResponse])
async def get_annotations_by_image(image_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching annotations for image_id={image_id}")
    annotations = db.query(Annotation).filter(Annotation.image_id == image_id).all()
    if not annotations:
        logger.warning(f"No annotations found for image_id={image_id}")
        raise HTTPException(status_code=404, detail="No annotations found for this image")
    return annotations

@router.put("/{id}", response_model=AnnotationResponse)
def update_annotation(id: int, annotation: AnnotationCreate, db: Session = Depends(get_db)):
    logger.info(f"Updating annotation id={id}")
    db_annotation = db.query(Annotation).filter(Annotation.id == id).first()
    if not db_annotation:
        logger.warning(f"Annotation id={id} not found for update")
        raise HTTPException(status_code=404, detail="Annotation not found")
    for key, value in annotation.model_dump().items():
        setattr(db_annotation, key, value)
    db.commit()
    db.refresh(db_annotation)
    return db_annotation

@router.delete("/{id}")
def delete_annotation(id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting annotation id={id}")
    db_annotation = db.query(Annotation).filter(Annotation.id == id).first()
    if not db_annotation:
        logger.warning(f"Annotation id={id} not found for delete")
        raise HTTPException(status_code=404, detail="Annotation not found")
    db.delete(db_annotation)
    db.commit()
    return {"detail": "Annotation deleted successfully"}

import logging
from fastapi import APIRouter, Depends, Query
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import Literal
from database import get_db
from models import Annotation
from schemas import AnnotationResponse
import csv
import io

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/{image_id}")
async def export_annotations(
    image_id: int,
    format: Literal["csv", "json"] = Query("json", description="Export format: csv or json"),
    db: Session = Depends(get_db)
):
    logger.info(f"Exporting annotations for image_id={image_id} in format={format}")
    annotations = db.query(Annotation).filter(Annotation.image_id == image_id).all()

    if format == "json":
        return [AnnotationResponse.model_validate(annotation) for annotation in annotations]

    elif format == "csv":
        if not annotations:
            logger.warning(f"No annotations found for image_id={image_id}")
            return PlainTextResponse("id,image_id,user_id,label,x,y,width,height,created_at\n", media_type="text/csv")

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "image_id", "user_id", "label", "x", "y", "width", "height", "created_at"])
        for annotation in annotations:
            writer.writerow([
                annotation.id,
                annotation.image_id,
                annotation.user_id,
                annotation.label,
                annotation.x,
                annotation.y,
                annotation.width,
                annotation.height,
                annotation.created_at.isoformat()
            ])
        csv_content = output.getvalue()
        output.close()
        return PlainTextResponse(csv_content, media_type="text/csv")

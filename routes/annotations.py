from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_annotations():
    """Get all annotations"""
    return {"message": "Annotations endpoint", "data": []}

@router.post("/")
async def create_annotation():
    """Create a new annotation"""
    return {"message": "Annotation created", "id": 1}

@router.get("/{annotation_id}")
async def get_annotation(annotation_id: int):
    """Get a specific annotation"""
    return {"message": f"Annotation {annotation_id}", "id": annotation_id}

@router.put("/{annotation_id}")
async def update_annotation(annotation_id: int):
    """Update an annotation"""
    return {"message": f"Annotation {annotation_id} updated", "id": annotation_id}

@router.delete("/{annotation_id}")
async def delete_annotation(annotation_id: int):
    """Delete an annotation"""
    return {"message": f"Annotation {annotation_id} deleted", "id": annotation_id}
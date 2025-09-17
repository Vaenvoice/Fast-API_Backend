from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_export_options():
    """Get available export options"""
    return {"message": "Export options", "formats": ["json", "csv", "xml"]}

@router.post("/json")
async def export_json():
    """Export data as JSON"""
    return {"message": "JSON export initiated", "format": "json"}

@router.post("/csv")
async def export_csv():
    """Export data as CSV"""
    return {"message": "CSV export initiated", "format": "csv"}

@router.post("/xml")
async def export_xml():
    """Export data as XML"""
    return {"message": "XML export initiated", "format": "xml"}
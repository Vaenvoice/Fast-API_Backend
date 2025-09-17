from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.annotations import router as annotations_router
from routes.images import router as images_router
from routes.export import router as export_router
from routes.ai import router as ai_router

app = FastAPI(
    title="FastAPI Project",
    description="A FastAPI project with organized routes",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health endpoint
@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Service is running"}

# Mount routers
app.include_router(annotations_router, prefix="/api/annotations", tags=["annotations"])
app.include_router(images_router, prefix="/api/images", tags=["images"])
app.include_router(export_router, prefix="/api/export", tags=["export"])
app.include_router(ai_router, prefix="/api/ai", tags=["ai"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
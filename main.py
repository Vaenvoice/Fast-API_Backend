from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.annotations import router as annotations_router
from routes.images import router as images_router
from routes.export import router as export_router
from routes.ai import router as ai_router

app = FastAPI(
    title="FastAPI Project",
    description="A FastAPI project with organized routes",
    version="1.0.0"
)

# Allow all origins (frontend can access backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {"msg": "Backend is running 🚀"}

# Health endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}

# Mount API routers
app.include_router(annotations_router, prefix="/api/annotations", tags=["annotations"])
app.include_router(images_router, prefix="/api/images", tags=["images"])
app.include_router(export_router, prefix="/api/export", tags=["export"])
app.include_router(ai_router, prefix="/api/ai", tags=["ai"])

# Serve static folder (for DZI tiles)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)


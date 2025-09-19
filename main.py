from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

# Import your routers
from routes.annotations import router as annotations_router
from routes.images import router as images_router
from routes.export import router as export_router
from routes.ai import router as ai_router

# Import DB utils
from database import get_db
from database import Base, engine   # ✅ ensure tables auto-create
import models                       # ✅ import models so Base sees them

app = FastAPI(
    title="FastAPI Project",
    description="A FastAPI project with organized routes",
    version="1.0.0"
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Local frontend (Vite)
        "http://localhost:8080",  # Another dev port
        "https://your-frontend.vercel.app",  # Replace with deployed frontend
        "*"  # fallback for now
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Auto-create DB tables ---
Base.metadata.create_all(bind=engine)

# --- Root endpoint ---
@app.get("/")
async def root():
    return {"msg": "Backend is running 🚀"}

# --- Health check endpoint ---
@app.get("/health")
async def health():
    return {"status": "ok"}

# --- Test DB connection ---
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        result = db.execute("SELECT 1")
        return {"db_status": "ok", "result": result.scalar()}
    except Exception as e:
        return {"db_status": "error", "detail": str(e)}

# --- Include routers ---
app.include_router(annotations_router, prefix="/api/annotations", tags=["annotations"])
app.include_router(images_router, prefix="/api/images", tags=["images"])
app.include_router(export_router, prefix="/api/export", tags=["export"])
app.include_router(ai_router, prefix="/api/ai", tags=["ai"])

# --- Serve static folder for DZI tiles ---
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)


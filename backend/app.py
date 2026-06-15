from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import PROJECT_NAME, API_V1_STR
from database import init_db, get_db
from routes import auth, institute, students, id_cards, dashboard
from models import Admin
from routes.auth import get_password_hash

# Initialize database
init_db()

# Create FastAPI app
app = FastAPI(
    title=PROJECT_NAME,
    description="Student ID Card Generator System",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router)
app.include_router(institute.router)
app.include_router(students.router)
app.include_router(id_cards.router)
app.include_router(dashboard.router)


@app.on_event("startup")
async def startup_event():
    """Initialize admin user if not exists"""
    from database import SessionLocal
    db = SessionLocal()
    
    admin_exists = db.query(Admin).first()
    if not admin_exists:
        # Create default admin (username: admin, password: admin123)
        hashed_password = get_password_hash("admin123")
        admin = Admin(
            username="admin",
            email="admin@school.com",
            hashed_password=hashed_password,
            full_name="Administrator",
            is_active=True
        )
        db.add(admin)
        db.commit()
        print("Default admin created: username=admin, password=admin123")
    
    db.close()


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Student ID Card Generator System",
        "version": "1.0.0",
        "api_docs": "/docs"
    }


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

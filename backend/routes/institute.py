from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, status
from sqlalchemy.orm import Session
from database import get_db
from models import Institute
from schemas import Institute as InstituteSchema, InstituteCreate, InstituteUpdate
from utils.image_handler import save_logo, save_signature
import config

router = APIRouter(prefix="/api/v1/institute", tags=["institute"])


@router.get("/settings", response_model=InstituteSchema)
async def get_institute_settings(db: Session = Depends(get_db)):
    """Get institute settings"""
    institute = db.query(Institute).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    return institute


@router.post("/settings", response_model=InstituteSchema)
async def create_institute_settings(
    institute: InstituteCreate,
    db: Session = Depends(get_db)
):
    """Create or update institute settings"""
    existing = db.query(Institute).first()
    
    if existing:
        for key, value in institute.dict(exclude_unset=True).items():
            setattr(existing, key, value)
        db.commit()
        db.refresh(existing)
        return existing
    
    new_institute = Institute(**institute.dict())
    db.add(new_institute)
    db.commit()
    db.refresh(new_institute)
    return new_institute


@router.put("/settings/{institute_id}", response_model=InstituteSchema)
async def update_institute(
    institute_id: int,
    institute_data: InstituteUpdate,
    db: Session = Depends(get_db)
):
    """Update institute settings"""
    institute = db.query(Institute).filter(Institute.id == institute_id).first()
    
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    for key, value in institute_data.dict(exclude_unset=True).items():
        if value is not None:
            setattr(institute, key, value)
    
    db.commit()
    db.refresh(institute)
    return institute


@router.post("/upload-logo")
async def upload_logo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload institute logo"""
    institute = db.query(Institute).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    try:
        content = await file.read()
        logo_path = save_logo(content, file.filename)
        
        institute.logo_path = logo_path
        db.commit()
        
        return {"message": "Logo uploaded successfully", "path": logo_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/upload-watermark")
async def upload_watermark(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload watermark"""
    institute = db.query(Institute).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    try:
        content = await file.read()
        watermark_path = save_logo(content, file.filename)
        
        institute.watermark_path = watermark_path
        db.commit()
        
        return {"message": "Watermark uploaded successfully", "path": watermark_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/upload-signature")
async def upload_signature(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload principal signature"""
    institute = db.query(Institute).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    try:
        content = await file.read()
        signature_path = save_signature(content, file.filename)
        
        institute.principal_signature_path = signature_path
        db.commit()
        
        return {"message": "Signature uploaded successfully", "path": signature_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

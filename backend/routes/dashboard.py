from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Student, GeneratedCard
from schemas import DashboardStats

router = APIRouter(prefix="/api/v1/dashboard", tags=["dashboard"])


@router.get("/stats/{institute_id}", response_model=DashboardStats)
async def get_dashboard_stats(institute_id: int, db: Session = Depends(get_db)):
    """Get dashboard statistics"""
    
    # Count total students
    total_students = db.query(Student).filter(Student.institute_id == institute_id).count()
    
    # Count students with photos
    students_with_photos = db.query(Student).filter(
        (Student.institute_id == institute_id) &
        (Student.photo_path.isnot(None))
    ).count()
    
    # Missing photos
    missing_photos = total_students - students_with_photos
    
    # Count generated cards
    total_cards_generated = db.query(GeneratedCard).filter(
        GeneratedCard.institute_id == institute_id
    ).count()
    
    return DashboardStats(
        total_students=total_students,
        total_photos_uploaded=students_with_photos,
        missing_photos=missing_photos,
        total_cards_generated=total_cards_generated,
        recent_activity=[
            {"type": "cards_generated", "count": total_cards_generated},
            {"type": "photos_uploaded", "count": students_with_photos},
            {"type": "missing_photos", "count": missing_photos},
        ]
    )

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import get_db
from models import Student, Institute, GeneratedCard
from utils.id_card_generator import generate_id_card_png
from utils.pdf_generator import generate_id_card_pdf, generate_pdf_report
from datetime import datetime
import os
import uuid
import config

router = APIRouter(prefix="/api/v1/id-cards", tags=["id-cards"])


@router.post("/generate-single/{student_id}")
async def generate_single_card(
    student_id: int,
    format: str = "both",  # png, pdf, both
    db: Session = Depends(get_db)
):
    """Generate ID card for single student"""
    
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    institute = db.query(Institute).filter(Institute.id == student.institute_id).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    try:
        card_id = str(uuid.uuid4())[:8]
        student_data = {
            "student_id": student.student_id,
            "name": student.name,
            "class_name": student.class_name,
            "roll_number": student.roll_number,
            "address": student.address,
            "photo_path": student.photo_path,
        }
        
        institute_data = {
            "name": institute.name,
            "logo_path": institute.logo_path,
            "watermark_path": institute.watermark_path,
            "principal_signature_path": institute.principal_signature_path,
        }
        
        result = {"student_id": student.student_id}
        
        # Generate PNG
        if format in ["png", "both"]:
            png_path = config.GENERATED_CARDS_DIR / f"{student.student_id}_{card_id}.png"
            generate_id_card_png(student_data, institute_data, str(png_path))
            result["png_path"] = str(png_path)
        
        # Generate PDF
        if format in ["pdf", "both"]:
            pdf_path = config.GENERATED_CARDS_DIR / f"{student.student_id}_{card_id}.pdf"
            generate_id_card_pdf(student_data, institute_data, str(pdf_path))
            result["pdf_path"] = str(pdf_path)
        
        # Save to database
        card_record = GeneratedCard(
            student_id=student.id,
            institute_id=institute.id,
            png_path=result.get("png_path"),
            pdf_path=result.get("pdf_path"),
            issue_date=datetime.now()
        )
        
        db.add(card_record)
        db.commit()
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-class/{class_name}")
async def generate_class_cards(
    class_name: str,
    institute_id: int,
    format: str = "both",
    db: Session = Depends(get_db)
):
    """Generate ID cards for entire class"""
    
    students = db.query(Student).filter(
        (Student.class_name == class_name) &
        (Student.institute_id == institute_id)
    ).all()
    
    if not students:
        raise HTTPException(status_code=404, detail="No students found in this class")
    
    institute = db.query(Institute).filter(Institute.id == institute_id).first()
    
    results = []
    errors = []
    
    for student in students:
        try:
            card_response = await generate_single_card(student.id, format, db)
            results.append(card_response)
        except Exception as e:
            errors.append(f"Error for {student.name}: {str(e)}")
    
    return {
        "message": f"Generated {len(results)} cards",
        "total_students": len(students),
        "generated": len(results),
        "errors": errors,
        "results": results
    }


@router.post("/generate-all/{institute_id}")
async def generate_all_cards(
    institute_id: int,
    format: str = "both",
    db: Session = Depends(get_db)
):
    """Generate ID cards for all students"""
    
    students = db.query(Student).filter(Student.institute_id == institute_id).all()
    
    if not students:
        raise HTTPException(status_code=404, detail="No students found")
    
    results = []
    errors = []
    
    for student in students:
        try:
            card_response = await generate_single_card(student.id, format, db)
            results.append(card_response)
        except Exception as e:
            errors.append(f"Error for {student.name}: {str(e)}")
    
    return {
        "message": f"Generated {len(results)} cards",
        "total_students": len(students),
        "generated": len(results),
        "errors": errors
    }


@router.get("/download/{file_name}")
async def download_card(file_name: str):
    """Download generated card file"""
    
    file_path = config.GENERATED_CARDS_DIR / file_name
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        filename=file_name,
        media_type="image/png" if file_name.endswith(".png") else "application/pdf"
    )


@router.get("/list/{institute_id}")
async def list_generated_cards(institute_id: int, db: Session = Depends(get_db)):
    """List all generated cards for institute"""
    
    cards = db.query(GeneratedCard).filter(GeneratedCard.institute_id == institute_id).all()
    
    return {
        "total": len(cards),
        "cards": [
            {
                "id": card.id,
                "student_id": card.student.student_id,
                "student_name": card.student.name,
                "png_path": card.png_path,
                "pdf_path": card.pdf_path,
                "generated_at": card.generated_at
            }
            for card in cards
        ]
    }

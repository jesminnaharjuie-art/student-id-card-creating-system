from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Student, Institute
from schemas import Student as StudentSchema, StudentCreate, StudentUpdate
from utils.image_handler import save_photo
from utils.excel_processor import parse_excel_students, validate_students
from utils.zip_handler import extract_photos_from_zip
import uuid
import config

router = APIRouter(prefix="/api/v1/students", tags=["students"])


def generate_student_id(class_name: str) -> str:
    """Generate unique student ID"""
    # Format: YYYY-CLASS-UNIQUE
    year = datetime.now().year
    unique = str(uuid.uuid4())[:8].upper()
    return f"{year}-{class_name}-{unique}"


@router.get("/", response_model=List[StudentSchema])
async def list_students(
    institute_id: int = None,
    class_name: str = None,
    search: str = None,
    db: Session = Depends(get_db)
):
    """List all students with optional filters"""
    query = db.query(Student)
    
    if institute_id:
        query = query.filter(Student.institute_id == institute_id)
    
    if class_name:
        query = query.filter(Student.class_name == class_name)
    
    if search:
        query = query.filter(
            (Student.name.ilike(f"%{search}%")) |
            (Student.student_id.ilike(f"%{search}%")) |
            (Student.roll_number.ilike(f"%{search}%"))
        )
    
    return query.all()


@router.get("/{student_id}", response_model=StudentSchema)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    """Get student details"""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/", response_model=StudentSchema)
async def create_student(
    student_data: StudentCreate,
    institute_id: int,
    db: Session = Depends(get_db)
):
    """Create new student"""
    institute = db.query(Institute).filter(Institute.id == institute_id).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    # Generate student ID
    student_id = generate_student_id(student_data.class_name)
    
    new_student = Student(
        **student_data.dict(),
        institute_id=institute_id,
        student_id=student_id
    )
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.put("/{student_id}", response_model=StudentSchema)
async def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    """Update student"""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for key, value in student_data.dict(exclude_unset=True).items():
        if value is not None:
            setattr(student, key, value)
    
    db.commit()
    db.refresh(student)
    return student


@router.post("/upload-photo/{student_id}")
async def upload_student_photo(
    student_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload student photo"""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    try:
        content = await file.read()
        photo_path = save_photo(content, f"{student.student_id}_{file.filename}")
        
        student.photo_path = photo_path
        db.commit()
        
        return {"message": "Photo uploaded successfully", "path": photo_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/bulk-import")
async def bulk_import_students(
    institute_id: int,
    excel_file: UploadFile = File(...),
    photos_zip: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    """
    Bulk import students from Excel and ZIP of photos
    
    Excel format: Class | Roll | Name | Age | Address | Image Name
    """
    institute = db.query(Institute).filter(Institute.id == institute_id).first()
    if not institute:
        raise HTTPException(status_code=404, detail="Institute not found")
    
    try:
        # Parse Excel
        excel_content = await excel_file.read()
        students_data, excel_errors = parse_excel_students(excel_content)
        
        if excel_errors:
            return {
                "message": "Import completed with errors",
                "errors": excel_errors,
                "imported": 0
            }
        
        # Validate students
        students_data, validation_errors = validate_students(students_data)
        
        # Extract photos if provided
        photos = {}
        if photos_zip:
            zip_content = await photos_zip.read()
            photos = extract_photos_from_zip(zip_content)
        
        # Create student records
        imported_count = 0
        import_errors = list(validation_errors)
        
        for student_data in students_data:
            try:
                student_id = generate_student_id(student_data["class_name"])
                
                new_student = Student(
                    student_id=student_id,
                    institute_id=institute_id,
                    name=student_data["name"],
                    class_name=student_data["class_name"],
                    roll_number=student_data["roll_number"],
                    age=student_data.get("age"),
                    address=student_data.get("address", ""),
                )
                
                # Try to find and save photo
                image_name = student_data.get("image_name")
                if image_name and image_name in photos:
                    try:
                        photo_path = save_photo(photos[image_name], f"{student_id}_{image_name}")
                        new_student.photo_path = photo_path
                    except Exception as e:
                        import_errors.append(f"Photo error for {student_data['name']}: {str(e)}")
                
                db.add(new_student)
                imported_count += 1
            except Exception as e:
                import_errors.append(f"Error importing {student_data['name']}: {str(e)}")
        
        db.commit()
        
        return {
            "message": "Bulk import completed",
            "imported": imported_count,
            "total": len(students_data),
            "errors": import_errors
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Delete student"""
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()
    
    return {"message": "Student deleted successfully"}


from datetime import datetime

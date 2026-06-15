from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


# Auth Schemas
class AdminLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Institute Schemas
class InstituteCreate(BaseModel):
    name: str
    address: str
    phone: str
    email: str
    website: Optional[str] = None


class InstituteUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    card_template: Optional[str] = None


class InstituteSettings(BaseModel):
    card_issue_date: Optional[datetime] = None
    card_expiry_date: Optional[datetime] = None


class Institute(BaseModel):
    id: int
    name: str
    address: str
    phone: str
    email: str
    website: Optional[str]
    logo_path: Optional[str]
    watermark_path: Optional[str]
    principal_signature_path: Optional[str]
    
    class Config:
        from_attributes = True


# Student Parent Schemas
class StudentParentCreate(BaseModel):
    father_name: Optional[str] = None
    father_nid: Optional[str] = None
    father_phone: Optional[str] = None
    father_occupation: Optional[str] = None
    mother_name: Optional[str] = None
    mother_nid: Optional[str] = None
    mother_phone: Optional[str] = None
    mother_occupation: Optional[str] = None
    guardian_name: Optional[str] = None
    guardian_relation: Optional[str] = None
    guardian_phone: Optional[str] = None
    emergency_contact: Optional[str] = None
    email: Optional[str] = None
    present_address: Optional[str] = None
    permanent_address: Optional[str] = None


class StudentParent(StudentParentCreate):
    id: int
    student_id: int
    
    class Config:
        from_attributes = True


# Student Schemas
class StudentCreate(BaseModel):
    name: str
    class_name: str
    roll_number: str
    section: Optional[str] = None
    address: str
    date_of_birth: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    religion: Optional[str] = None
    nationality: Optional[str] = None
    admission_date: Optional[str] = None
    session: Optional[str] = None


class StudentUpdate(StudentCreate):
    name: Optional[str] = None
    class_name: Optional[str] = None
    roll_number: Optional[str] = None
    address: Optional[str] = None


class Student(StudentCreate):
    id: int
    student_id: str
    institute_id: int
    photo_path: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


# Generated Card Schemas
class GeneratedCardCreate(BaseModel):
    student_id: int
    template_id: Optional[str] = "default"


class GeneratedCard(BaseModel):
    id: int
    student_id: int
    png_path: Optional[str]
    pdf_path: Optional[str]
    issue_date: datetime
    expiry_date: Optional[datetime]
    
    class Config:
        from_attributes = True


# Dashboard Schema
class DashboardStats(BaseModel):
    total_students: int
    total_photos_uploaded: int
    missing_photos: int
    total_cards_generated: int
    recent_activity: List[dict] = []

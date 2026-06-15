from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    full_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Institute(Base):
    __tablename__ = "institutes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True)
    address = Column(String(500))
    phone = Column(String(20))
    email = Column(String(100))
    website = Column(String(200), nullable=True)
    logo_path = Column(String(500), nullable=True)
    watermark_path = Column(String(500), nullable=True)
    principal_signature_path = Column(String(500), nullable=True)
    card_issue_date = Column(DateTime, nullable=True)
    card_expiry_date = Column(DateTime, nullable=True)
    card_template = Column(String(50), default="default")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    students = relationship("Student", back_populates="institute")
    generated_cards = relationship("GeneratedCard", back_populates="institute")


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(50), unique=True, index=True)
    institute_id = Column(Integer, ForeignKey("institutes.id"))
    name = Column(String(200), index=True)
    class_name = Column(String(50))
    roll_number = Column(String(50))
    section = Column(String(10), nullable=True)
    date_of_birth = Column(String(20), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)
    blood_group = Column(String(10), nullable=True)
    religion = Column(String(50), nullable=True)
    nationality = Column(String(100), nullable=True)
    address = Column(String(500))
    photo_path = Column(String(500), nullable=True)
    admission_date = Column(String(20), nullable=True)
    session = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    institute = relationship("Institute", back_populates="students")
    parent_info = relationship("StudentParent", uselist=False, back_populates="student")
    documents = relationship("StudentDocument", back_populates="student")
    generated_cards = relationship("GeneratedCard", back_populates="student")


class StudentParent(Base):
    __tablename__ = "student_parents"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), unique=True)
    father_name = Column(String(100), nullable=True)
    father_nid = Column(String(50), nullable=True)
    father_phone = Column(String(20), nullable=True)
    father_occupation = Column(String(100), nullable=True)
    mother_name = Column(String(100), nullable=True)
    mother_nid = Column(String(50), nullable=True)
    mother_phone = Column(String(20), nullable=True)
    mother_occupation = Column(String(100), nullable=True)
    guardian_name = Column(String(100), nullable=True)
    guardian_relation = Column(String(50), nullable=True)
    guardian_phone = Column(String(20), nullable=True)
    guardian_nid = Column(String(50), nullable=True)
    emergency_contact = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    present_address = Column(String(500), nullable=True)
    permanent_address = Column(String(500), nullable=True)
    
    student = relationship("Student", back_populates="parent_info")


class StudentDocument(Base):
    __tablename__ = "student_documents"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    birth_certificate = Column(String(500), nullable=True)
    father_nid_file = Column(String(500), nullable=True)
    mother_nid_file = Column(String(500), nullable=True)
    document_type = Column(String(100), nullable=True)
    file_path = Column(String(500))
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    student = relationship("Student", back_populates="documents")


class GeneratedCard(Base):
    __tablename__ = "generated_cards"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    institute_id = Column(Integer, ForeignKey("institutes.id"))
    png_path = Column(String(500), nullable=True)
    pdf_path = Column(String(500), nullable=True)
    template_id = Column(String(50), default="default")
    issue_date = Column(DateTime, default=datetime.utcnow)
    expiry_date = Column(DateTime, nullable=True)
    generated_at = Column(DateTime, default=datetime.utcnow)
    
    student = relationship("Student", back_populates="generated_cards")
    institute = relationship("Institute", back_populates="generated_cards")


class Settings(Base):
    __tablename__ = "settings"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(100), unique=True, index=True)
    value = Column(Text)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

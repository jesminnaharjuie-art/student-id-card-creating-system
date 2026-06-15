import pandas as pd
import io
from typing import List, Tuple


def parse_excel_students(file_content: bytes) -> Tuple[List[dict], List[str]]:
    """
    Parse Excel file and extract student data
    
    Expected columns: Class, Roll, Name, Age, Address, Image Name
    
    Returns: (students_list, errors_list)
    """
    
    errors = []
    students = []
    
    try:
        # Read Excel
        df = pd.read_excel(io.BytesIO(file_content))
        
        # Validate columns
        required_columns = ["Class", "Roll", "Name", "Age", "Address", "Image Name"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            errors.append(f"Missing columns: {', '.join(missing_columns)}")
            return students, errors
        
        # Process rows
        for idx, row in df.iterrows():
            try:
                # Validate required fields
                if pd.isna(row["Name"]) or pd.isna(row["Class"]) or pd.isna(row["Roll"]):
                    errors.append(f"Row {idx + 2}: Missing Name, Class, or Roll")
                    continue
                
                student = {
                    "name": str(row["Name"]).strip(),
                    "class_name": str(row["Class"]).strip(),
                    "roll_number": str(row["Roll"]).strip(),
                    "age": int(row["Age"]) if pd.notna(row["Age"]) else None,
                    "address": str(row["Address"]).strip() if pd.notna(row["Address"]) else "",
                    "image_name": str(row["Image Name"]).strip() if pd.notna(row["Image Name"]) else None,
                }
                
                students.append(student)
            except Exception as e:
                errors.append(f"Row {idx + 2}: {str(e)}")
        
        return students, errors
    
    except Exception as e:
        errors.append(f"Excel parsing error: {str(e)}")
        return [], errors


def validate_students(students: List[dict]) -> Tuple[List[dict], List[str]]:
    """
    Validate student data for duplicates and invalid entries
    """
    
    errors = []
    validated = []
    seen_rolls = set()
    
    for student in students:
        # Check for duplicate roll numbers
        key = f"{student['class_name']}-{student['roll_number']}"
        if key in seen_rolls:
            errors.append(f"Duplicate: Class {student['class_name']}, Roll {student['roll_number']}")
            continue
        
        seen_rolls.add(key)
        validated.append(student)
    
    return validated, errors

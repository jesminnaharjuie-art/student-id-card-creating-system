from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from datetime import datetime
import os


def generate_id_card_pdf(
    student_data: dict,
    institute_data: dict,
    output_path: str
) -> str:
    """
    Generate ID card as PDF
    
    Card size: 3.5" x 2.25" (standard ID card)
    """
    
    # Create PDF with custom page size (3.5 x 2.25 inches)
    card_width = 3.5 * inch
    card_height = 2.25 * inch
    
    c = canvas.Canvas(output_path, pagesize=(card_width, card_height))
    
    # Background
    c.setFillColor(HexColor("#FFFFFF"))
    c.rect(0, 0, card_width, card_height, fill=1, stroke=1)
    
    # Border
    c.setStrokeColor(HexColor("#0F172A"))
    c.setLineWidth(2)
    c.rect(10, 10, card_width - 20, card_height - 20)
    
    # Institute name (top)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(HexColor("#0F172A"))
    inst_name = institute_data.get("name", "Institute")[:30]
    c.drawString(20, card_height - 25, inst_name)
    
    # Student ID
    c.setFont("Helvetica", 9)
    c.drawString(20, card_height - 40, f"ID: {student_data.get('student_id', 'N/A')}")
    
    # Name
    c.setFont("Helvetica-Bold", 11)
    name = student_data.get("name", "N/A")[:25]
    c.drawString(20, card_height - 55, name)
    
    # Class and Roll
    c.setFont("Helvetica", 9)
    c.drawString(20, card_height - 70, f"Class: {student_data.get('class_name', 'N/A')}")
    c.drawString(1.8 * inch, card_height - 70, f"Roll: {student_data.get('roll_number', 'N/A')}")
    
    # Address (truncated)
    c.setFont("Helvetica", 8)
    address = student_data.get("address", "N/A")[:35]
    c.drawString(20, card_height - 85, f"Address: {address}")
    
    # Issue date
    c.setFont("Helvetica", 7)
    issue_date = datetime.now().strftime("%d/%m/%Y")
    c.drawString(20, card_height - 100, f"Issued: {issue_date}")
    
    # Add logo if exists
    if institute_data.get("logo_path") and os.path.exists(institute_data["logo_path"]):
        try:
            c.drawImage(
                institute_data["logo_path"],
                card_width - 60,
                card_height - 45,
                width=50,
                height=30,
                preserveAspectRatio=True
            )
        except:
            pass
    
    # Add photo if exists
    if student_data.get("photo_path") and os.path.exists(student_data["photo_path"]):
        try:
            c.drawImage(
                student_data["photo_path"],
                card_width - 100,
                card_height - 110,
                width=0.8 * inch,
                height=1.1 * inch,
                preserveAspectRatio=True
            )
        except:
            pass
    
    c.save()
    return output_path


def generate_pdf_report(
    cards_data: list,
    institute_data: dict,
    output_path: str
) -> str:
    """
    Generate PDF report with multiple ID cards
    """
    
    # Create multi-page PDF
    card_width = 3.5 * inch
    card_height = 2.25 * inch
    
    c = canvas.Canvas(output_path, pagesize=(card_width * 2, card_height * 3))
    
    positions = [
        (20, card_height * 2.8),
        (card_width + 20, card_height * 2.8),
        (20, card_height * 1.5),
        (card_width + 20, card_height * 1.5),
        (20, 20),
        (card_width + 20, 20),
    ]
    
    for idx, card_data in enumerate(cards_data):
        if idx > 0 and idx % 6 == 0:
            c.showPage()
        
        pos_idx = idx % 6
        x, y = positions[pos_idx]
        
        # Draw card background
        c.setFillColor(HexColor("#FFFFFF"))
        c.rect(x, y, card_width - 40, card_height - 10, fill=1, stroke=1)
        
        # Border
        c.setStrokeColor(HexColor("#0F172A"))
        c.setLineWidth(1)
        c.rect(x + 5, y + 5, card_width - 50, card_height - 20)
        
        # Content
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(HexColor("#0F172A"))
        c.drawString(x + 10, y + card_height - 20, institute_data.get("name", "Institute")[:20])
        
        c.setFont("Helvetica", 7)
        c.drawString(x + 10, y + card_height - 30, f"ID: {card_data.get('student_id', 'N/A')}")
        
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x + 10, y + card_height - 42, card_data.get('name', 'N/A')[:20])
        
        c.setFont("Helvetica", 6)
        c.drawString(x + 10, y + card_height - 52, f"Class: {card_data.get('class_name', 'N/A')}")
        c.drawString(x + 1.3 * inch + x, y + card_height - 52, f"Roll: {card_data.get('roll_number', 'N/A')}")
    
    c.save()
    return output_path

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
import config
from .image_handler import get_image_or_placeholder
from .qr_generator import generate_qr_code


def generate_id_card_png(
    student_data: dict,
    institute_data: dict,
    output_path: str
) -> str:
    """
    Generate ID card as PNG image
    
    student_data: {name, class_name, roll_number, address, photo_path, student_id}
    institute_data: {name, logo_path, watermark_path, principal_signature_path}
    """
    
    # Card dimensions (3.5" x 2.25" at 300 DPI = 1050 x 675 pixels)
    card_width = 1050
    card_height = 675
    
    # Create blank card
    card = Image.new("RGB", (card_width, card_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(card)
    
    # Load or create placeholder fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 28)
        header_font = ImageFont.truetype("arial.ttf", 24)
        normal_font = ImageFont.truetype("arial.ttf", 18)
        small_font = ImageFont.truetype("arial.ttf", 14)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        normal_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Left side: Photo section
    photo_width = 300
    photo_height = 400
    photo = get_image_or_placeholder(
        student_data.get("photo_path"),
        photo_width,
        photo_height
    )
    card.paste(photo, (20, 120))
    
    # Right side: Information section
    right_x = 350
    
    # Institute logo (top right)
    if institute_data.get("logo_path") and os.path.exists(institute_data["logo_path"]):
        try:
            logo = Image.open(institute_data["logo_path"])
            logo.thumbnail((80, 60), Image.Resampling.LANCZOS)
            card.paste(logo, (900, 20))
        except:
            pass
    
    # Institute name
    draw.text(
        (right_x, 30),
        institute_data.get("name", "Institute Name"),
        fill=(0, 0, 0),
        font=header_font
    )
    
    # Student ID
    draw.text(
        (right_x, 80),
        f"ID: {student_data.get('student_id', 'N/A')}",
        fill=(0, 0, 0),
        font=normal_font
    )
    
    # Name
    draw.text(
        (right_x, 130),
        f"Name: {student_data.get('name', 'N/A')}",
        fill=(0, 0, 0),
        font=normal_font
    )
    
    # Class and Roll
    draw.text(
        (right_x, 180),
        f"Class: {student_data.get('class_name', 'N/A')} | Roll: {student_data.get('roll_number', 'N/A')}",
        fill=(0, 0, 0),
        font=small_font
    )
    
    # Address
    address = student_data.get("address", "N/A")
    if len(address) > 40:
        address = address[:40] + "..."
    draw.text(
        (right_x, 230),
        f"Address: {address}",
        fill=(0, 0, 0),
        font=small_font
    )
    
    # QR Code
    qr_data = student_data.get("student_id", "unknown")
    qr_img = generate_qr_code(qr_data, size=120)
    card.paste(qr_img, (850, 400))
    
    # Issue and Expiry dates
    draw.text(
        (right_x, 580),
        f"Issued: {datetime.now().strftime('%d/%m/%Y')}",
        fill=(0, 0, 0),
        font=small_font
    )
    
    # Watermark if available
    if institute_data.get("watermark_path") and os.path.exists(institute_data["watermark_path"]):
        try:
            watermark = Image.open(institute_data["watermark_path"])
            watermark.thumbnail((500, 500), Image.Resampling.LANCZOS)
            watermark.putalpha(int(255 * 0.15))  # 15% opacity
            card.paste(watermark, (250, 150), watermark)
        except:
            pass
    
    # Save card
    card.save(output_path, quality=95)
    return output_path

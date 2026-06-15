import qrcode
import io
from PIL import Image


def generate_qr_code(data: str, size: int = 200) -> Image.Image:
    """
    Generate QR code from string data
    Returns PIL Image object
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size), Image.Resampling.LANCZOS)
    return img


def get_qr_as_bytes(data: str, size: int = 200) -> bytes:
    """Generate QR code and return as bytes"""
    img = generate_qr_code(data, size)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes.getvalue()

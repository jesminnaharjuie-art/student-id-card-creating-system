import io
import os
from PIL import Image
from pathlib import Path
import config


def save_photo(file_content: bytes, filename: str) -> str:
    """Save student photo and return file path"""
    file_path = config.PHOTO_DIR / filename
    
    # Open and validate image
    try:
        img = Image.open(io.BytesIO(file_content))
        # Resize to standard dimension (300x400 for ID cards)
        img = img.resize((300, 400), Image.Resampling.LANCZOS)
        img.save(file_path, quality=95)
        return str(file_path)
    except Exception as e:
        raise ValueError(f"Invalid image file: {str(e)}")


def save_logo(file_content: bytes, filename: str) -> str:
    """Save institute logo and return file path"""
    file_path = config.LOGO_DIR / filename
    
    try:
        img = Image.open(io.BytesIO(file_content))
        img = img.resize((200, 100), Image.Resampling.LANCZOS)
        img.save(file_path, quality=95)
        return str(file_path)
    except Exception as e:
        raise ValueError(f"Invalid logo file: {str(e)}")


def save_signature(file_content: bytes, filename: str) -> str:
    """Save principal signature and return file path"""
    file_path = config.SIGNATURE_DIR / filename
    
    try:
        img = Image.open(io.BytesIO(file_content))
        img = img.resize((150, 60), Image.Resampling.LANCZOS)
        img.save(file_path, quality=95)
        return str(file_path)
    except Exception as e:
        raise ValueError(f"Invalid signature file: {str(e)}")


def resize_image(image_path: str, width: int, height: int) -> Image.Image:
    """Load and resize image"""
    img = Image.open(image_path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return img


def get_image_or_placeholder(image_path: str, width: int, height: int) -> Image.Image:
    """Get image or return placeholder"""
    try:
        if image_path and os.path.exists(image_path):
            return resize_image(image_path, width, height)
    except:
        pass
    
    # Create placeholder image
    placeholder = Image.new("RGB", (width, height), color=(200, 200, 200))
    return placeholder


def save_document(file_content: bytes, filename: str) -> str:
    """Save student document and return file path"""
    file_path = config.DOCUMENT_DIR / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, "wb") as f:
        f.write(file_content)
    
    return str(file_path)

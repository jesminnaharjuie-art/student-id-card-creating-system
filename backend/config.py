import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
PHOTO_DIR = UPLOAD_DIR / "photos"
DOCUMENT_DIR = UPLOAD_DIR / "documents"
LOGO_DIR = UPLOAD_DIR / "logos"
SIGNATURE_DIR = UPLOAD_DIR / "signatures"
GENERATED_CARDS_DIR = UPLOAD_DIR / "generated_cards"

# Create directories if they don't exist
PHOTO_DIR.mkdir(parents=True, exist_ok=True)
DOCUMENT_DIR.mkdir(parents=True, exist_ok=True)
LOGO_DIR.mkdir(parents=True, exist_ok=True)
SIGNATURE_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_CARDS_DIR.mkdir(parents=True, exist_ok=True)

# Database
DATABASE_URL = f"sqlite:///{BASE_DIR}/sims.db"

# Security
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

# File uploads
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB
ALLOWED_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png"}
ALLOWED_DOCUMENT_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}
ALLOWED_EXCEL_EXTENSIONS = {"xlsx", "xls"}

# ID Card Settings
CARD_WIDTH = 3.5  # inches
CARD_HEIGHT = 2.25  # inches
QR_CODE_SIZE = 150  # pixels

# API Settings
API_V1_STR = "/api/v1"
PROJECT_NAME = "Student ID Card Generator"

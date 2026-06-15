import zipfile
import io
from pathlib import Path
from typing import Dict, List


def extract_photos_from_zip(
    zip_content: bytes,
    allowed_extensions: set = None
) -> Dict[str, bytes]:
    """
    Extract all photos from ZIP file
    
    Returns: {filename: file_content}
    """
    
    if allowed_extensions is None:
        allowed_extensions = {"jpg", "jpeg", "png"}
    
    photos = {}
    
    try:
        with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
            for file_info in zip_file.filelist:
                # Skip directories and hidden files
                if file_info.filename.endswith("/"):
                    continue
                
                if file_info.filename.startswith("__MACOSX"):
                    continue
                
                # Check extension
                ext = Path(file_info.filename).suffix.lower().lstrip(".")
                if ext not in allowed_extensions:
                    continue
                
                # Get filename only (ignore folder structure)
                filename = Path(file_info.filename).name
                
                # Read file content
                content = zip_file.read(file_info.filename)
                photos[filename] = content
    
    except Exception as e:
        raise ValueError(f"Invalid ZIP file: {str(e)}")
    
    return photos


def list_zip_contents(zip_content: bytes) -> List[str]:
    """
    List all files in ZIP
    """
    
    files = []
    
    try:
        with zipfile.ZipFile(io.BytesIO(zip_content)) as zip_file:
            for file_info in zip_file.filelist:
                if not file_info.filename.endswith("/"):
                    files.append(file_info.filename)
    except Exception as e:
        raise ValueError(f"Invalid ZIP file: {str(e)}")
    
    return files

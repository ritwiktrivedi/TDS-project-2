import os
import zipfile
from pathlib import Path

def unzip_folder(zip_path, extract_to=None):
    
    zip_path = Path(zip_path)

    if not zip_path.exists():
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    if extract_to is None:
        extract_to = zip_path.parent
    else:
        extract_to = Path(extract_to)
        os.makedirs(extract_to, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    return str(extract_to)
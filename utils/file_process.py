import os
import zipfile
from pathlib import Path

def unzip_folder(zip_path, extract_to=None, matched_files=None):
    zip_path = Path(zip_path)

    if not zip_path.exists():
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    if extract_to is None:
        extract_to = zip_path.parent
    else:
        extract_to = Path(extract_to)
        os.makedirs(extract_to, exist_ok=True)

    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"The file provided is not a valid zip file: {zip_path}")

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    if matched_files:
        extracted_files = [f.name for f in extract_to.iterdir() if f.is_file()]
        extracted_files.sort() 
        matched_files.sort()

        if len(extracted_files) != len(matched_files):
            raise ValueError(
                f"Number of extracted files ({len(extracted_files)}) does not match number of matched files ({len(matched_files)})."
            )

        for extracted_file, new_name in zip(extracted_files, matched_files):
            old_path = extract_to / extracted_file
            new_path = extract_to / new_name

            if not new_path.exists(): 
                old_path.rename(new_path)
            else:
                raise FileExistsError(f"Target file already exists: {new_path}")

    return str(extract_to)

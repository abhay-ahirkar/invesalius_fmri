import os
import nibabel as nib

def read_nifti_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    img = nib.load(file_path)
    data = img.get_fdata()
    return data

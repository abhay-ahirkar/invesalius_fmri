import os
import nibabel as nib

def read_nifti_file(file_path):
    # Read the NIFTI file
    data = nib.load(file_path).get_fdata()

    # Return the data
    return data

def main():
    # Get the current working directory
    cwd = os.getcwd()

    # Get the file path
    file_path = os.path.join(cwd, "data", "fmri.nii.gz")

    # Read the NIFTI file
    data = read_nifti_file(file_path)

    # Print the data
    print(data)

if __name__ == "__main__":

    # Run the main function
    main()



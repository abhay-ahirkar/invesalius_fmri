import nibabel as nib

class NiftiReader(Reader):
    def __init__(self):
        super().__init__()

    def Read(self, filename):
        """
        Reads a NIFTI file and returns the image data
        """
        image = nib.load(filename)

        # Extract the image data
        data = image.get_fdata()

        # Extract the TR
        tr = image.header.get_zooms()[3]

        # Extract the dimensions of the fMRI volume
        fmri_dims = data.shape[:-1]

        # Create a dictionary to hold the fMRI-specific data
        fmri_info = {
            "tr": tr,
            "fmri_dims": fmri_dims
        }

        return data, fmri_info

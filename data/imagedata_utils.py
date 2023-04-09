import math
import sys
import tempfile
import gdcm
import imageio
import numpy
import numpy as np
from scipy.ndimage import shift, zoom
from vtkmodules.util import numpy_support
from vtkmodules.vtkFiltersCore import vtkImageAppend
from vtkmodules.vtkImagingCore import vtkExtractVOI, vtkImageClip, vtkImageResample
from vtkmodules.vtkImagingGeneral import vtkImageGaussianSmooth
from vtkmodules.vtkInteractionImage import vtkImageViewer
from vtkmodules.vtkIOXML import vtkXMLImageDataReader, vtkXMLImageDataWriter


def get_image_data_from_file(file_path):
    """
    Get image data from file.
    :param file_path: The file path.
    :return: The image data.
    """

    # Get the file extension
    file_extension = file_path.split(".")[-1]

    # Check if the file extension is DICOM
    if file_extension == "dcm" or file_extension == "dicom":
        # Read the DICOM file
        reader = gdcm.ImageReader()
        reader.SetFileName(file_path)
        reader.Read()

        # Get the image
        image = reader.GetImage()

        # Get the image data
        image_data = image.GetBuffer()

        # Get the image dimensions
        image_dimensions = image.GetDimensions()

        # Get the image spacing
        image_spacing = image.GetSpacing()

        # Get the image origin
        image_origin = image.GetOrigin()

        # Get the image direction
        image_direction = image.GetDirectionCosines()

        # Get the image data type
        image_data_type = image.GetPixelFormat().GetScalarTypeAsString()

        # Get the image data type
        if image_data_type == "UINT8":
            image_data_type = numpy.uint8
        elif image_data_type == "INT8":
            image_data_type = numpy.int8
        elif image_data_type == "UINT16":
            image_data_type = numpy.uint16
        elif image_data_type == "INT16":
            image_data_type = numpy.int16
        elif image_data_type == "UINT32":
            image_data_type = numpy.uint32
        elif image_data_type == "INT32":
            image_data_type = numpy.int32
        elif image_data_type == "FLOAT32":
            image_data_type = numpy.float32
        elif image_data_type == "FLOAT64":
            image_data_type = numpy.float64

        # Get the image data
        image_data = numpy.frombuffer(image_data, dtype=image_data_type)

        # Reshape the image data
        image_data = image_data.reshape(image_dimensions, order="F")

        # Get the image data
        image_data = numpy.swapaxes(image_data, 0, 2)

        # Get the image data
        image_data = numpy.flip(image_data, 0)

        # Get the image data
        image_data = numpy.flip(image_data, 1)

        # Get the image data
        image_data = numpy.flip(image_data, 2)

        # Get the image data
        image_data = numpy.rot90(image_data, 1, (0, 1))


    # Check if the file extension is NIFTI

    elif file_extension == "nii" or file_extension == "nii.gz":
        # Read the NIFTI file
        image_data = nib.load(file_path).get_fdata()

        # Get the image data
        image_data = numpy.swapaxes(image_data, 0, 2)

        # Get the image data
        image_data = numpy.flip(image_data, 0)

        # Get the image data
        image_data = numpy.flip(image_data, 1)

        # Get the image data
        image_data = numpy.flip(image_data, 2)

        # Get the image data
        image_data = numpy.rot90(image_data, 1, (0, 1))

    




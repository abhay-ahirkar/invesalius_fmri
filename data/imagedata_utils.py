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


def read_image(file_name):
    reader = vtkXMLImageDataReader()
    reader.SetFileName(file_name)
    reader.Update()
    return reader.GetOutput()


def write_image(image_data, file_name):
    writer = vtkXMLImageDataWriter()
    writer.SetFileName(file_name)
    writer.SetInputData(image_data)
    writer.Write()


def resize_image(image_data, factor):
    shape = image_data.GetDimensions()
    new_shape = [math.ceil(factor * dim) for dim in shape]
    resampled_data = vtkImageResample()
    resampled_data.SetInputData(image_data)
    resampled_data.SetOutputDimensions(new_shape)
    resampled_data.Update()
    return resampled_data.GetOutput()


def clip_image(image_data, lower_threshold, upper_threshold):
    clipper = vtkImageClip()
    clipper.SetInputData(image_data)
    clipper.ClipDataOn()
    clipper.InsideOutOn()
    clipper.SetOutputScalarTypeToUnsignedChar()
    clipper.SetClipDataScalarRange(lower_threshold, upper_threshold)
    clipper.Update()
    return clipper.GetOutput()


def smooth_image(image_data, kernel_size):
    smoother = vtkImageGaussianSmooth()
    smoother.SetInputData(image_data)
    smoother.SetStandardDeviations(kernel_size, kernel_size, kernel_size)
    smoother.Update()
    return smoother.GetOutput()


def extract_voi(image_data, voi):
    extractor = vtkExtractVOI()
    extractor.SetInputData(image_data)
    extractor.SetVOI(voi)
    extractor.Update()
    return extractor.GetOutput()


def append_images(image_list):
    appender = vtkImageAppend()
    for image in image_list:
        appender.AddInputData(image)
    appender.Update()
    return appender.GetOutput()


def save_as_video(image_data, output_path, fps):
    shape = image_data.GetDimensions()
    writer = imageio.get_writer(output_path, fps=fps)
    for i in range(shape[0]):
        slice_data = vtkExtractVOI()
        slice_data.SetInputData(image_data)
        slice_data.SetVOI(i, i, 0, shape[1] - 1, 0, shape[2] - 1)
        slice_data.Update()
        slice_np = numpy_support.vtk_to_numpy(slice_data.GetOutput().GetPointData().GetScalars())
        slice_np = slice_np.reshape((shape[1], shape[2]))
        slice_np = (slice_np / np.max(slice_np) * 255).astype(np.uint8)
        writer.append_data(slice_np)
    writer.close()

# code for others_reader.py  to read NIFTI file (of FMRI)
##impoeort the necessary packages
import os
import nibabel as nib
from vtkmodules.vtkCommonCore import vtkFileOutputWindow, vtkOutputWindow
from vtkmodules.util import numpy_support
from vtkmodules.vtkCommonDataModel import vtkImageData

## function to read nifti file
def read_nifti_file(file_path):
    img = nib.load(file_path)
    data = img.get_fdata()
    return data

## function to convert nifti file to vtkImageData
def nifti_to_vtk(path):


    vtkOutputWindow.SetInstance(vtkFileOutputWindow())
    vtkOutputWindow.GetInstance().SetFileName("vtk.log")
    vtkOutputWindow.GetInstance().SetInstance(vtkFileOutputWindow())
    vtkOutputWindow.GetInstance().SetFileName("vtk.log")

    data = read_nifti_file(path)
    data = numpy_support.numpy_to_vtk(num_array=data.ravel(), deep=True, array_type=vtkImageData.GetScalarType(data.dtype))
    data.SetNumberOfComponents(1)
    data.SetNumberOfTuples(data.GetNumberOfTuples())
    data.Update()

    img = vtkImageData()
    img.SetDimensions(data.GetNumberOfTuples(), 1, 1)
    img.GetPointData().SetScalars(data)
    img.Update()

    return img

## function to read nifti file and convert it to vtkImageData
def read_nifti(path):

    vtkOutputWindow.SetInstance(vtkFileOutputWindow())
    vtkOutputWindow.GetInstance().SetFileName("vtk.log")
    vtkOutputWindow.GetInstance().SetInstance(vtkFileOutputWindow())
    vtkOutputWindow.GetInstance().SetFileName("vtk.log")

    data = read_nifti_file(path)
    data = numpy_support.numpy_to_vtk(num_array=data.ravel(), deep=True, array_type=vtkImageData.GetScalarType(data.dtype))
    data.SetNumberOfComponents(1)
    data.SetNumberOfTuples(data.GetNumberOfTuples())
    data.Update()

    img = vtkImageData()
    img.SetDimensions(data.GetNumberOfTuples(), 1, 1)
    img.GetPointData().SetScalars(data)
    img.Update()

    return img


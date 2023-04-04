
# InVesalius fMRI Support

This project aims to add functional MRI (fMRI) support to InVesalius, an open-source software for medical imaging. Currently, InVesalius only supports the visualization of structural MRI (sMRI) data. By adding fMRI support, users will be able to visualize and analyze functional brain activity, enabling more advanced medical research and diagnoses.

## Implementation Plan

The project will be divided into the following tasks:

1.  Create a new task for fMRI functionality called `task_fmri.py` in the `invesalius/gui` folder using wxPython.
2.  Modify the `others_reader.py` module to read and load NIFTI files.
3.  Modify the `viewer_slice.py` module to display fMRI data in slices.
4.  Modify the `viewer_volume.py` module to display 3D reconstructions of the fMRI region of interest.
5.  Implement the user interface for fMRI parameters by creating a new panel in the InVesalius GUI.
6.  Implement visualization features for fMRI by adding a new menu item to the InVesalius GUI that allows users to display statistical maps of the fMRI data.

## Features

The following features will be implemented:

-   User interface to support and control fMRI parameters, such as slice selection, smoothing, and thresholding
-   Visualization features for fMRI, including the ability to display statistical maps, such as t-maps and z-maps
-   Real-time visualization of the fMRI data as the parameters are adjusted
-   Support for displaying fMRI data as an overlay on the anatomical MRI data
-   Support for displaying the fMRI data in 3D and providing tools for adjusting the 3D visualization

## Future Additions

The following features may be added in the future:

-   Integration with other medical imaging software to allow for more advanced analysis and visualization
-   Support for other fMRI-specific data formats, such as DICOM
-   Integration with machine learning and artificial intelligence algorithms for automated analysis and diagnosis

## Screenshots and Videos

Sample screenshots and videos will be provided as the project progresses.
![alt text](https://github.com/abhay-ahirkar/invesalius_fmri/blob/master/media/Screenshot%202023-04-04%20150338.jpg?raw=true)



## Installation

To install InVesalius with fMRI support, follow these steps:

1.  Clone this repository
2.  Navigate to the `invesalius_fmri` directory
3.  Install the required dependencies by running `pip install -r requirements.txt`
4.  Run InVesalius by running `python invesalius.py`

## Contributing

Contributions are welcome! Please fork this repository and create a new branch for your changes. Once you've made your changes, create a pull request and we'll review it as soon as possible.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

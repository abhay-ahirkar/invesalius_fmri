import wx
import os
import numpy as np
import nibabel as nib
from invesalius.gui.task import Task

class FMRITask(Task):
    """
    A new task for fMRI functionality that extends the base Task class
    """

    def __init__(self, parent):
        """
        Initializes the FMRITask object
        """
        Task.__init__(self, parent)

        # Define fMRI-specific attributes
        self.fmri_data = None
        self.fmri_overlay = None
        self.fmri_threshold = None
        self.fmri_smoothing = None
        self.fmri_slice = None

        # Create the GUI elements
        self.fmri_panel = wx.Panel(self)
        self.fmri_sizer = wx.BoxSizer(wx.VERTICAL)

        self.fmri_slice_label = wx.StaticText(self.fmri_panel, label="Slice:")
        self.fmri_slice_slider = wx.Slider(self.fmri_panel, style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS)
        self.fmri_threshold_label = wx.StaticText(self.fmri_panel, label="Threshold:")
        self.fmri_threshold_slider = wx.Slider(self.fmri_panel, style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS)
        self.fmri_smoothing_label = wx.StaticText(self.fmri_panel, label="Smoothing:")
        self.fmri_smoothing_slider = wx.Slider(self.fmri_panel, style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS)

        self.fmri_sizer.Add(self.fmri_slice_label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        self.fmri_sizer.Add(self.fmri_slice_slider, 0, wx.EXPAND|wx.ALL, 5)
        self.fmri_sizer.Add(self.fmri_threshold_label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        self.fmri_sizer.Add(self.fmri_threshold_slider, 0, wx.EXPAND|wx.ALL, 5)
        self.fmri_sizer.Add(self.fmri_smoothing_label, 0, wx.ALIGN_LEFT|wx.ALL, 5)
        self.fmri_sizer.Add(self.fmri_smoothing_slider, 0, wx.EXPAND|wx.ALL, 5)

        self.fmri_panel.SetSizer(self.fmri_sizer)

        # Connect the GUI elements to event handlers
        self.Bind(wx.EVT_SCROLL, self.OnSliceSlider, self.fmri_slice_slider)
        self.Bind(wx.EVT_SCROLL, self.OnThresholdSlider, self.fmri_threshold_slider)
        self.Bind(wx.EVT_SCROLL, self.OnSmoothingSlider, self.fmri_smoothing_slider)

    def OnSliceSlider(self, event):
        """
        Event handler for the fMRI slice slider
        """
        self.fmri_slice = self.fmri_slice_slider.GetValue()
        self.UpdateFMRI()

    def OnThresholdSlider(self, event):
        """
        Event handler for the fMRI threshold slider
        """
        self.fmri_threshold = self.fmri_threshold_slider.GetValue()
        self.UpdateFMRI()

    def OnSmoothingSlider(self, event):
        """
        Event handler for the fMRI smoothing slider
        """
        self.fmri_smoothing = self.fmri_smoothing_slider.GetValue()
        self.UpdateFMRI()

    def UpdateFMRI(self):
        """
        Updates the fMRI visualization based on the current fMRI parameters
        """
        # TODO: Implement fMRI visualization functionality
        pass

    def LoadFMRI(self, filename):
        """
        Loads the fMRI data from a NIFTI file
        """
        if os.path.exists(filename):
            # Load the NIFTI file
            fmri_image = nib.load(filename)
            fmri_data = fmri_image.get_fdata()

            # Update the fMRI-specific attributes
            self.fmri_data = fmri_data
            self.fmri_overlay = np.zeros_like(fmri_data)
            self.fmri_threshold = np.max(fmri_data) / 2
            self.fmri_smoothing = 0
            self.fmri_slice = fmri_data.shape[2] // 2

            # Update the GUI elements
            self.fmri_slice_slider.SetRange(0, fmri_data.shape[2] - 1)
            self.fmri_slice_slider.SetValue(self.fmri_slice)
            self.fmri_threshold_slider.SetRange(0, np.max(fmri_data))
            self.fmri_threshold_slider.SetValue(self.fmri_threshold)
            self.fmri_smoothing_slider.SetRange(0, 10)
            self.fmri_smoothing_slider.SetValue(self.fmri_smoothing)

            # Update the fMRI visualization
            self.UpdateFMRI()

def OnLoad(self, event):
    """
    Event handler for the load button
    """
    # TODO: Implement file loading functionality
    pass

def OnSave(self, event):
    """
    Event handler for the save button
    """
    # TODO: Implement file saving functionality
    pass

def OnExport(self, event):
    """
    Event handler for the export button
    """
    # TODO: Implement file exporting functionality
    pass

def OnClose(self, event):
    """
    Event handler for the close button
    """
    # TODO: Implement task closing functionality
    pass

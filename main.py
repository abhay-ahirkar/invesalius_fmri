import wx
import os
import sys

from gui.task_fmri import TaskFMRI
from reader.others_reader import read_nifti
from data.viewer_slice import ViewerSlice
from data.viewer_volume import ViewerVolume


class FMRIViewer(wx.Frame):
    def __init__(self, parent, title):
        super(FMRIViewer, self).__init__(parent, title=title, size=(800, 600))
        
        # Set up the GUI
        self.task_fmri = TaskFMRI(self)
        self.viewer_slice = ViewerSlice(self)
        self.viewer_volume = ViewerVolume(self)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.task_fmri, 0, wx.EXPAND)
        self.sizer.Add(self.viewer_slice, 1, wx.EXPAND)
        self.sizer.Add(self.viewer_volume, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        
        self.Center()
        self.Show()


def main():
    # Initialize the application
    app = wx.App()
    
    # Create the main window
    frame = FMRIViewer(None, "fMRI Viewer")
    
    # Show the window
    frame.Show()
    
    # Run the application
    app.MainLoop()


if __name__ == '__main__':
    main()

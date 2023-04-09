# Path: gui\task_fmri.py
import wx
from wx.lib.agw import foldpanelbar as fpb
from wx.lib.agw import ultimatelistctrl as ulc

class TaskFMRI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Create file picker
        self.file_picker = wx.FilePickerCtrl(self, message="Select a NIFTI file")
        
        # Create load button
        self.load_button = wx.Button(self, label="Load")
        
        # Create view panel
        self.view_panel = wx.Panel(self)
        
        # Create view sizer
        self.view_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.view_panel.SetSizer(self.view_sizer)
        
        # Create slice radio button
        self.slice_radio = wx.RadioButton(self.view_panel, label="Slice view")
        
        # Create volume radio button
        self.volume_radio = wx.RadioButton(self.view_panel, label="Volume view")
        
        # Create display panel
        self.display_panel = wx.Panel(self)
        
        # Create display sizer
        self.display_sizer = wx.BoxSizer(wx.VERTICAL)
        self.display_panel.SetSizer(self.display_sizer)
        
        # Create slice viewer
        self.slice_viewer = None
        
        # Create volume viewer
        self.volume_viewer = None
        
        # Set sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.file_picker, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.load_button, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.view_panel, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.display_panel, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
        
        # Bind events
        self.load_button.Bind(wx.EVT_BUTTON, self.on_load_button_click)
        self.slice_radio.Bind(wx.EVT_RADIOBUTTON, self.on_slice_radio_click)
        self.volume_radio.Bind(wx.EVT_RADIOBUTTON, self.on_volume_radio_click)
        
        # Disable the view panel and display panel initially
        self.view_panel.Enable(False)
        self.display_panel.Enable(False)
    
    def get_file_path(self):
        return self.file_picker.GetPath()
    
    def on_load_button_click(self, event):
        # Read the selected NIFTI file
        file_path = self.file_picker.GetPath()
        data = read_nifti_file(file_path)
        
        if data is not None:
            # Enable the view panel and display panel
            self.view_panel.Enable(True)    
            self.display_panel.Enable(True)

            # Create slice viewer
            self.slice_viewer = SliceViewer(self.display_panel)
            self.slice_viewer.set_data(data)

            # Create volume viewer
            self.volume_viewer = VolumeViewer(self.display_panel)
            self.volume_viewer.set_data(data)

            # Add slice viewer and volume viewer to the display sizer
            self.display_sizer.Add(self.slice_viewer, 1, wx.EXPAND | wx.ALL, 5)
            self.display_sizer.Add(self.volume_viewer, 1, wx.EXPAND | wx.ALL, 5)
            self.display_panel.Layout()

            # Disable the slice viewer and volume viewer initially
            self.slice_viewer.Enable(False)
            self.volume_viewer.Enable(False)

    def on_slice_radio_click(self, event):
        # Enable the slice viewer and disable the volume viewer
        self.slice_viewer.Enable(True)
        self.volume_viewer.Enable(False)

    def on_volume_radio_click(self, event):
        # Enable the volume viewer and disable the slice viewer
        self.slice_viewer.Enable(False)
        self.volume_viewer.Enable(True)

class SliceViewer(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create figure
        self.figure = Figure()

        # Create canvas
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Create toolbar
        self.toolbar = NavigationToolbar(self.canvas)

        # Create sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)

    def set_data(self, data):
        # Create axes
        self.axes = self.figure.add_subplot(111)

        # Create image
        self.image = self.axes.imshow(data[0])

        # Create title
        self.title = self.axes.set_title("Slice 0")

        # Create slider
        self.slider = wx.Slider(self, value=0, minValue=0, maxValue=data.shape[0] - 1)

        # Create sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.slider, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)

        # Bind events
        self.slider.Bind(wx.EVT_SLIDER, self.on_slider_change)

    def on_slider_change(self, event):
        # Get the current value of the slider
        value = self.slider.GetValue()

        # Update the image
        self.image.set_data(self.data[value])

        # Update the title
        self.title.set_text(f"Slice {value}")

        # Redraw the canvas
        self.canvas.draw()

class VolumeViewer(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # Create figure
        self.figure = Figure()

        # Create canvas
        self.canvas = FigureCanvas(self, -1, self.figure)

        # Create toolbar
        self.toolbar = NavigationToolbar(self.canvas)

        # Create sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)

    def set_data(self, data):
        # Create axes
        self.axes = self.figure.add_subplot(111, projection="3d")

        # Create image
        self.image = self.axes.imshow(data[0])

        # Create title
        self.title = self.axes.set_title("Slice 0")

        # Create slider
        self.slider = wx.Slider(self, value=0, minValue=0, maxValue=data.shape[0] - 1)

        # Create sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.toolbar, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.slider, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)

        # Bind events
        self.slider.Bind(wx.EVT_SLIDER, self.on_slider_change)

    def on_slider_change(self, event):
        # Get the current value of the slider
        value = self.slider.GetValue()

        # Update the image
        self.image.set_data(self.data[value])

        # Update the title
        self.title.set_text(f"Slice {value}")

        # Redraw the canvas
        self.canvas.draw()

def read_nifti_file(file_path):
    try:
        # Read the NIFTI file
        data = nib.load(file_path).get_fdata()

        # Return the data
        return data
    except:
        # Display error message
        wx.MessageBox("Error reading NIFTI file.", "Error", wx.OK | wx.ICON_ERROR)

        # Return None
        return None


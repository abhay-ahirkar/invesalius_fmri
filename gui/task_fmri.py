import wx
import wx.lib.agw.foldpanelbar as fpb

from data.viewer_slice import SliceViewer
from data.viewer_volume import VolumeViewer
from reader.others_reader import read_nifti_file


class TaskFMRI(fpb.FoldPanelBar):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0, agwStyle=fpb.FPB_COLLAPSE_TO_BOTTOM):
        super().__init__(parent, id=id, pos=pos, size=size, style=style, agwStyle=agwStyle)

        # Create a panel for loading NIFTI file
        fp = self.AddFoldPanel("Load NIFTI file", collapsed=True)
        self.load_panel = wx.Panel(fp)
        self.load_sizer = wx.BoxSizer(wx.VERTICAL)
        self.load_panel.SetSizer(self.load_sizer)

        # Add a file picker control to select NIFTI file
        self.file_picker = wx.FilePickerCtrl(self.load_panel, message="Select NIFTI file")
        self.load_sizer.Add(self.file_picker, 0, wx.ALL|wx.EXPAND, 5)

        # Add a button to load the selected NIFTI file
        self.load_button = wx.Button(self.load_panel, label="Load")
        self.load_button.Bind(wx.EVT_BUTTON, self.on_load_button_click)
        self.load_sizer.Add(self.load_button, 0, wx.ALL|wx.EXPAND, 5)

        # Create a panel for selecting slice view or volume view
        fp = self.AddFoldPanel("Select view type", collapsed=True)
        self.view_panel = wx.Panel(fp)
        self.view_sizer = wx.BoxSizer(wx.VERTICAL)
        self.view_panel.SetSizer(self.view_sizer)

        # Add a radio button to select slice view
        self.slice_radio = wx.RadioButton(self.view_panel, label="Slice view", style=wx.RB_GROUP)
        self.slice_radio.SetValue(True)
        self.view_sizer.Add(self.slice_radio, 0, wx.ALL|wx.EXPAND, 5)

        # Add a radio button to select volume view
        self.volume_radio = wx.RadioButton(self.view_panel, label="Volume view")
        self.view_sizer.Add(self.volume_radio, 0, wx.ALL|wx.EXPAND, 5)

        # Add a panel for displaying the selected view
        fp = self.AddFoldPanel("View", collapsed=True)
        self.display_panel = wx.Panel(fp)
        self.display_sizer = wx.BoxSizer(wx.VERTICAL)
        self.display_panel.SetSizer(self.display_sizer)

        # Create slice viewer and volume viewer instances
        self.slice_viewer = SliceViewer(self.display_panel)
        self.volume_viewer = VolumeViewer(self.display_panel)

        # Add slice viewer and volume viewer to display sizer
        self.display_sizer.Add(self.slice_viewer, 1, wx.ALL|wx.EXPAND, 5)
        self.display_sizer.Add(self.volume_viewer, 1, wx.ALL|wx.EXPAND, 5)

        # Disable the view panel and display panel initially
        self.view_panel.Enable(False)
        self.display_panel.Enable(False)

    def on_load_button_click(self, event):
        # Read the selected NIFTI file
        file_path = self.file_picker.GetPath()
        data = read_nifti_file(file_path)

        if data is not None:
            # Enable the view panel and display panel
            self.view_panel.Enable(True)
            self.display_panel.Enable(True)

            if self.slice_radio.GetValue():
                # Show slice viewer if slice view is selected
                self.volume_viewer.Hide()
                self.slice_viewer.Show()
                self.slice_viewer.set_data(data)
            else:
                # Show volume viewer if volume view is selected
                self.slice_viewer.Hide()
                self.volume_viewer.Show()
                self.volume_viewer.set_data(data)

            # Update the display panel
            self.display_panel.Layout()

    def on_slice_radio_click(self, event):
        # Show slice viewer if slice view is selected
        self.volume_viewer.Hide()
        self.slice_viewer.Show()

        # Update the display panel
        self.display_panel.Layout()

    def on_volume_radio_click(self, event):
        # Show volume viewer if volume view is selected
        self.slice_viewer.Hide()
        self.volume_viewer.Show()

        # Update the display panel
        self.display_panel.Layout()





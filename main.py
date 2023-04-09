import wx
from gui.task_fmri import TaskFMRI
from reader.others_reader import read_nifti_file
from data.viewer_slice import SliceViewer
from data.imagedata_utils import *
from data.viewer_volume import VolumeViewer

class InvesaliusFMRI(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, title="Invesalius FMRI")
        self.panel = wx.Panel(self.frame)
        
        # Create task panel
        self.task_panel = TaskFMRI(self.panel)
        
        # Create slice viewer
        self.slice_viewer = SliceViewer(self.panel)
        
        # Create volume viewer
        self.volume_viewer = VolumeViewer(self.panel)
        
        # Bind events
        self.task_panel.Bind(wx.EVT_BUTTON, self.on_load_button)
        self.slice_viewer.Bind(wx.EVT_SCROLL, self.on_slice_scroll)
        self.volume_viewer.Bind(wx.EVT_SCROLL, self.on_volume_scroll)
        
        # Set sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.task_panel, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.slice_viewer, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.volume_viewer, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)
        
        self.frame.Show()
        return True
    
    def on_load_button(self, event):
        file_path = self.task_panel.get_file_path()
        if file_path:
            self.data = read_nifti_file(file_path)
            self.slice_viewer.set_data(self.data)
            self.volume_viewer.set_data(self.data)
    
    def on_slice_scroll(self, event):
        slice_num = self.slice_viewer.get_slice_number()
        self.volume_viewer.set_slice_number(slice_num)
    
    def on_volume_scroll(self, event):
        slice_num = self.volume_viewer.get_slice_number()
        self.slice_viewer.set_slice_number(slice_num)

if __name__ == "__main__":
    app = InvesaliusFMRI()
    app.MainLoop()


#
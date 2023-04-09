# Path: gui\volume_viewer.py
import wx
import wx.lib.agw.aui as aui
import wx.lib.agw.customtreectrl as CT

class VolumeViewer(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Create volume viewer
        self.volume_viewer = wx.Panel(self)
        
        # Set sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.volume_viewer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
    
    def set_data(self, data):
        pass




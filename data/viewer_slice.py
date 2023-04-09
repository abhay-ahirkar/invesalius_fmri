# Path: gui\slice_viewer.py
import wx
import wx.lib.agw.aui as aui
import wx.lib.agw.customtreectrl as CT
import wx.lib.agw.flatnotebook as fnb
import wx.lib.agw.hyperlink as hl
import wx.lib.agw.pybusyinfo as PBI
import wx.lib.agw.pycollapsiblepane as PCP
import wx.lib.agw.pygauge as PG
import wx.lib.agw.pyprogress as PP
import wx.lib.agw.ribbon as RB
import wx.lib.agw.shapedbutton as SB
import wx.lib.agw.toasterbox as TB
import wx.lib.agw.ultimatelistctrl as ULC
import wx.lib.agw.ultimatelistctrl as ULC

class SliceViewer(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Create slice slider
        self.slice_slider = wx.Slider(self, style=wx.SL_HORIZONTAL)
        
        # Create slice viewer
        self.slice_viewer = wx.Panel(self)
        
        # Set sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.slice_slider, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.slice_viewer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
        
        # Bind events
        self.slice_slider.Bind(wx.EVT_SCROLL, self.on_slice_scroll)
    
    def get_slice_number(self):
        return self.slice_slider.GetValue()
    
    def on_slice_scroll(self, event):
        pass
    
    def set_data(self, data):
        pass
    
    def set_slice_number(self, slice_num):
        self.slice_slider.SetValue(slice_num)


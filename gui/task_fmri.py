import sys
import os

import wx

try:
    import wx.lib.agw.hyperlink as hl
    import wx.lib.agw.foldpanelbar as fpb
except ImportError:
    import wx.lib.hyperlink as hl
    import wx.lib.foldpanelbar as fpb

class TaskFMRI(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # TODO: Add GUI elements and functionality

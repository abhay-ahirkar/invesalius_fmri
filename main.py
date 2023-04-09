import wx
from gui.task_fmri import TaskFMRI

class InvesaliusFMRI(wx.App):
    def OnInit(self):
        frame = TaskFMRI(None, title='Invesalius fMRI')
        frame.Show()
        return True

if __name__ == '__main__':
    app = InvesaliusFMRI()
    app.MainLoop()

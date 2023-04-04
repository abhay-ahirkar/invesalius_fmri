import wx

class FMRIParameters(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        # Slice selection
        slice_label = wx.StaticText(self, label='Slice:')
        self.slice_slider = wx.Slider(self, value=0, minValue=0, maxValue=100, style=wx.SL_HORIZONTAL)
        slice_box = wx.BoxSizer(wx.HORIZONTAL)
        slice_box.Add(slice_label, flag=wx.ALIGN_CENTER_VERTICAL)
        slice_box.AddSpacer(10)
        slice_box.Add(self.slice_slider, proportion=1, flag=wx.EXPAND)
        self.slice_slider.Bind(wx.EVT_SCROLL, self.on_slice_selection)

    

        # Smoothing
        smooth_label = wx.StaticText(self, label='Smoothing:')
        self.smooth_slider = wx.Slider(self, value=0, minValue=0, maxValue=10, style=wx.SL_HORIZONTAL)
        smooth_box = wx.BoxSizer(wx.HORIZONTAL)
        smooth_box.Add(smooth_label, flag=wx.ALIGN_CENTER_VERTICAL)
        smooth_box.AddSpacer(10)
        smooth_box.Add(self.smooth_slider, proportion=1, flag=wx.EXPAND)

        # Bind events
        self.smooth_slider.Bind(wx.EVT_SLIDER, self.on_smooth_slider_changed)

    
        # 2D view
        self.view2d_button = wx.Button(self, label='2D View', size=(150, -1))
        self.view2d_button.Bind(wx.EVT_BUTTON, self.on_2d_view)

    

        # 3D view
        self.view3d_button = wx.Button(self, label='3D View', size=(150, -1))
        self.view3d_button.Bind(wx.EVT_BUTTON, self.on_3d_view)

    
   


        # Thresholding
        threshold_label = wx.StaticText(self, label='Thresholding:')
        self.threshold_slider = wx.Slider(self, value=0, minValue=0, maxValue=255, style=wx.SL_HORIZONTAL)
        threshold_box = wx.BoxSizer(wx.HORIZONTAL)
        threshold_box.Add(threshold_label, flag=wx.ALIGN_CENTER_VERTICAL)
        threshold_box.AddSpacer(10)
        threshold_box.Add(self.threshold_slider, proportion=1, flag=wx.EXPAND)

        self.threshold_slider.Bind(wx.EVT_SCROLL, self.on_threshold_scroll)

    


        # Apply button
        apply_button = wx.Button(self, label='Apply', size=(150, -1))
        apply_button.SetBackgroundColour(wx.Colour(0, 128, 0))
        apply_button.SetForegroundColour(wx.WHITE)

        

        

  

        # Add all the boxes to the main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(slice_box, flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)
        main_sizer.Add(smooth_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        main_sizer.Add(wx.StaticLine(self), flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=10)
        main_sizer.Add(self.view2d_button, flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        main_sizer.Add(self.view3d_button, flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        main_sizer.Add(wx.StaticLine(self), flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=10)
        main_sizer.Add(threshold_box, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        main_sizer.Add(apply_button, flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)

        self.SetSizer(main_sizer)

    def on_slice_selection(self, event):
        slice_value = self.slice_slider.GetValue()
            # Do something with the slice value, e.g. update a 2D or 3D view

    def apply_parameters(self, event):
        # Get the current values of the sliders and do something with them
        slice_value = self.slice_slider.GetValue()
        smooth_value = self.smooth_slider.GetValue()
        threshold_value = self.threshold_slider.GetValue()

    def on_threshold_scroll(self, event):
        threshold_value = self.threshold_slider.GetValue()
        self.threshold_label.SetLabel(f'Thresholding: {threshold_value}')
        event.Skip()

    def on_3d_view(self, event):
        # Code to show 3D view
        print("Showing 3D view...")

    def on_smooth_slider_changed(self, event):
        value = self.smooth_slider.GetValue()
        self.smooth_label.SetLabel(f'Smoothing: {value}')
        # TODO: Perform smoothing operation with selected value

    def on_2d_view(self, event):
        # Your code to handle the 2D view button click event goes here
        print("2D View button clicked")

    

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="InVesalius FMRI PRAMETERS", size=(400, 300))
        self.SetBackgroundColour(wx.WHITE)
        self.panel = FMRIParameters(self)
        self.panel.SetBackgroundColour(wx.WHITE)
        self.Show()
        
if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()

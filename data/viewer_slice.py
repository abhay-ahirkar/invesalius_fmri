import numpy as np
import matplotlib.pyplot as plt

class SliceViewer:
    def __init__(self, volume):
        self.volume = volume
        self.fig, self.ax = plt.subplots()
        self.index = volume.shape[0] // 2
        self.update()

    def update(self):
        self.ax.clear()
        self.ax.imshow(self.volume[self.index])
        self.ax.set_title(f"Slice {self.index}")
        self.fig.canvas.draw()

    def on_scroll(self, event):
        if event.button == 'up':
            self.index = (self.index + 1) % self.volume.shape[0]
        else:
            self.index = (self.index - 1) % self.volume.shape[0]
        self.update()

    def show(self):
        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        plt.show()

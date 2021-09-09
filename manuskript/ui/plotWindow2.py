import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=1, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

    def barplot(self, y, xticklabels):

        self.axes.bar(range(len(y)), y, width=1)
        self.axes.set_xticks(range(len(y)))
        self.axes.set_xticklabels(xticklabels)

        plt.setp(self.axes.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
        plt.subplots_adjust(bottom=0.4)
        #self.fig.tight_layout()

        #a = np.random.random((16, 16))
        #self.axes.imshow(a, cmap='hot', interpolation='nearest')

        #self.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        #self.show()

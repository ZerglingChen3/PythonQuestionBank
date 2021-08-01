import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as mp
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np
from list import problem_record as pr


class MyFigure(FigureCanvas):

    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

    def draw1(self):
        pro_type = ["单选题", "判断题", "简答题"]
        for type in pro_type:
            rate = pr[type]
            self.axes.bar(rate, y, alpha=0.5, width=0.3,
                          color='yellow', edgecolor='red', label=type, lw=3)
        # self.axes.bar(np.arange(16) + 0.4, y, alpha=0.2, width=0.3, color='green', edgecolor='blue', label='The Second Bar',
        #        lw=3)

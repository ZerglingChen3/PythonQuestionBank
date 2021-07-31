import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as mp
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np


class MyFigure(FigureCanvas):

    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(233)

    def plotsin(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plotcos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def drawHist(self):
        mp.rcParams['font.sans-serif'] = ['SimHei']
        # mp.rcParams['axes.unicode_minus'] = False

        apples = np.array([45, 46, 12, 45, 121, 65, 45, 60, 11, 56, 34, 54])
        oranges = np.array([54, 36, 82, 47, 96, 34, 45, 62, 85, 66, 94, 63])
        mp.figure('Bar Chart', facecolor='lightgray')
        mp.title('Bar Chart', fontsize=16)
        mp.xlabel('Month', fontsize=14)
        mp.ylabel('Volume', fontsize=14)
        mp.tick_params(labelsize=10)
        mp.grid(linestyle=':', axis='y')
        x = np.arange(12)
        a = mp.bar(x - 0.2, apples, 0.4, color='dodgerblue', label='Apple', align='center')
        b = mp.bar(x + 0.2, oranges, 0.4, color='orangered', label='Oranges', align='center')
        # 设置标签
        for i in a + b:
            h = i.get_height()
            mp.text(i.get_x() + i.get_width() / 2, h, '%d' % int(h), ha='center', va='bottom')
        mp.xticks(x, ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])

        mp.legend()
        mp.show()
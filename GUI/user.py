import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from .surface import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np


class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)

    # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plotsin(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)

    def plotcos(self):
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2 * np.pi * t)
        self.axes.plot(t, s)


class userInformationSurface(Surface):

    def __init__(self):
        super().__init__()
        self.information_widget = QWidget()
        self.information_layout = QGridLayout()
        self.information_widget.setLayout(self.information_layout)

        self.figureBox_widget = QGroupBox()
        self.figureBox_layout = QGridLayout()
        self.figureBox_widget.setLayout(self.figureBox_layout)

        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos()
        self.main_layout.addWidget(self.F, 0, 1, 3, 3)

        self.initUI()

    def receive_nameSignal(self, name):
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.logout_but, 1, 0)
        self.main_layout.addWidget(self.information_widget, 0, 6, 2, 2)

    def initUI(self):
        self.resize(1080, 960)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

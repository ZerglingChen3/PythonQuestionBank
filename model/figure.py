import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from model import list


class MyFigure(FigureCanvas):

    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def draw1(self):
        pro_type = ["单选题", "判断题", "简答题"]
        bar = []

        for type in pro_type:
            time, correct = list.problem_record[type].getTimes()
            if time == 0:
                rate = 0
            else:
                rate = correct / time

            x = [type]
            y = [rate]
            bar.append(self.axes.bar(x, y, alpha=0.5, width=0.3, color='yellow', edgecolor='red', label=type, lw=3))

        self.axes.set_ylim([0, 1])
        for bar_container in bar:
            for b in bar_container:
                height = b.get_height()
                self.axes.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.01, '%.2f' % height, ha='center',
                               va='bottom')

import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from model import list
import pandas as pd


class MyFigure(FigureCanvas):

    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def draw0(self):
        pro_type = ["单选题", "判断题"]
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

    def draw1(self):
        pro_type = ["单选题", "判断题"]
        bar = []

        for type in pro_type:
            time, correct = list.current_record[type][0], list.current_record[type][1]
            if time == 0:
                rate = 0
            else:
                rate = correct / time

            x = [type]
            y = [rate]
            bar.append(self.axes.bar(x, y, alpha=0.5, width=0.3, color='blue', edgecolor='green', label=type, lw=3))

        self.axes.set_ylim([0, 1])
        for bar_container in bar:
            for b in bar_container:
                height = b.get_height()
                self.axes.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.01, '%.2f' % height, ha='center',
                               va='bottom')

    def draw2(self, name):
        data_path = "./data/user/"
        current_path = data_path + str(name)
        current_excel = current_path + "/log.xlsx"

        df = pd.read_excel(current_excel)
        cnt = df.shape[0]
        x = []
        y = []
        bar = []

        for i in range(max(0, cnt - 4), cnt):
            line = df.loc[i].values
            x.append(line[1])
            y.append(line[8] / line[7])

        bar.append(self.axes.bar(x, y, alpha=0.5, width=0.3, color='blue', edgecolor='green', lw=3))
        self.axes.set_ylim([0, 1])
        for bar_container in bar:
            for b in bar_container:
                height = b.get_height()
                self.axes.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.01, '%.2f' % height, ha='center',
                               va='bottom')

    def draw3(self, name):
        data_path = "./data/user/"
        current_path = data_path + str(name)
        current_excel = current_path + "/log.xlsx"

        df = pd.read_excel(current_excel)
        cnt = df.shape[0]
        x = []
        y = []
        plot = []

        for i in range(max(0, cnt - 4), cnt):
            line = df.loc[i].values
            x.append(line[1])
            y.append(line[6] + line[7])

        plot.append(self.axes.plot(x, y))

    def draw4(self, name):
        data_path = "./data/user/"
        current_path = data_path + str(name)
        current_excel = current_path + "/log.xlsx"

        labels = ['单选题', '判断题', '简答题']
        tot = 0
        tot_singe = 0
        tot_judge = 0
        tot_easy = 0
        data = pd.read_excel(current_excel)
        for i in range(data.shape[0]):
            line = data.loc[i].values
            tot_singe += line[2]
            tot_judge += line[4]
            tot_easy += line[6]
            tot += line[2] + line[4] + line[6]

        size = [tot_singe, tot_judge, tot_easy]
        explode = (0.1, 0.1, 0.1)
        self.axes.pie(size, explode, labels=labels, autopct='%1.1f%%')

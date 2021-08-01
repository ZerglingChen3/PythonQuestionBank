import matplotlib

matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from .surface import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np

global surface


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
        y = range(1, 17)

        self.axes.bar(np.arange(16), y, alpha=0.5, width=0.3, color='yellow', edgecolor='red', label='The First Bar',
                      lw=3)
        self.axes.bar(np.arange(16) + 0.4, y, alpha=0.2, width=0.3, color='green', edgecolor='blue',
                      label='The Second Bar',
                      lw=3)
        self.axes.legend()
        # self.axes.plot(t, s)

    def drawhist(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # mp.rcParams['axes.unicode_minus'] = False

        apples = np.array([45, 46, 12, 45, 121, 65, 45, 60, 11, 56, 34, 54])
        oranges = np.array([54, 36, 82, 47, 96, 34, 45, 62, 85, 66, 94, 63])
        # plt.figure('Bar Chart', facecolor='lightgray')
        # self.axes.set('Bar Chart', fontsize=16)
        # self.axes.xlabel('Month', fontsize=14)
        # self.axes.ylabel('Volume', fontsize=14)
        self.axes.tick_params(labelsize=10)
        self.axes.grid(linestyle=':', axis='y')
        x = np.arange(12)
        a = plt.bar(x - 0.2, apples, 0.4, color='dodgerblue', label='Apple', align='center')
        b = plt.bar(x + 0.2, oranges, 0.4, color='orangered', label='Oranges', align='center')
        # 设置标签
        for i in a + b:
            h = i.get_height()
            self.axes.text(i.get_x() + i.get_width() / 2, h, '%d' % int(h), ha='center', va='bottom')
        # self.axes.xticks(x, ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])

        # self.axes.legend()
        # plt.show()


choose_list = ["历史各类题目正确率"]


class userInformationChooseSurface(Surface):

    def __init__(self):
        super().__init__()
        self.information_widget, self.information_layout = getWidget()
        self.password_group_widget, self.password_group_layout = getGroup("修改密码")
        self.password_widget, self.password_layout = getWidget()
        self.password_button_widget, self.password_button_layout = getWidget()
        self.combobox_widget, self.combobox_layout = getWidget()
        self.data_group_widget, self.data_group_layout = getGroup("查看个人数据")

        self.password_label = QLabel("新密码：")
        self.password_text = QLineEdit()
        self.password_but = QPushButton("确认")

        self.list = QComboBox()
        self.list_but = QPushButton("确认")

        self.logout_but = QPushButton("注销")
        """
        self.figureBox_widget = QGroupBox()
        self.figureBox_layout = QGridLayout()
        self.figureBox_widget.setLayout(self.figureBox_layout)

        self.F = MyFigure(width=3, height=2, dpi=100)
        self.F.plotcos()
        self.main_layout.addWidget(self.F, 0, 1, 3, 3)
        """

        self.initLabel()
        self.initPos()
        self.initList()
        self.initEvent()
        self.initUI()

    def initLabel(self):
        self.headLabel = QLabel("个人信息")
        self.headLabel.setAlignment(Qt.AlignHCenter)
        self.headLabel.setStyleSheet("color:rgb(60,60,60,255);"
                                     "font-size:100px;"
                                     "font-weight:bold;"
                                     "font-family:Roman"
                                     "times;")

    def initPos(self):
        self.main_layout.addWidget(self.headLabel, 0, 0, 9, 9)
        self.main_layout.addWidget(self.password_group_widget, 2, 0, 2, 4)
        self.password_group_layout.addWidget(self.password_widget, 0, 0, 1, 4)
        self.password_group_layout.addWidget(self.password_button_widget, 1, 0, 1, 2)
        self.password_layout.addWidget(self.password_label, 0, 0)
        self.password_layout.addWidget(self.password_text, 0, 1)
        self.password_button_layout.addWidget(self.password_but, 0, 0)
        self.main_layout.addWidget(self.data_group_widget, 4, 0, 2, 4)
        self.data_group_layout.addWidget(self.list, 0, 0)
        self.data_group_layout.addWidget(self.list_but, 1, 0)

    def initList(self):
        self.list.addItems(choose_list)

    def receive_nameSignal(self, name):
        print("当前用户名为:" + str(name))
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.logout_but, 1, 0)
        self.main_layout.addWidget(self.information_widget, 1, 5, 2, 2)

    def initUI(self):
        self.resize(1080, 960)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

    def initEvent(self):
        self.logout_but.clicked.connect(self.logout_but_clicked)
        self.password_but.clicked.connect(self.password_but_clicked)
        self.list_but.clicked.connect(self.list_but_clicked)

    def logout_but_clicked(self):
        from .login import loginSurface
        self.close()
        global surface
        surface = loginSurface()
        surface.show()

    def password_but_clicked(self):
        password = self.password_text.text()
        if password == "":
            QMessageBox.warning(self, '警告', "新密码不能为空，请重新输入！")
            return
        from manage import person as nps
        nps.changePassword(self.username, password)
        from .login import loginSurface
        self.close()
        global surface
        surface = loginSurface()
        surface.show()

    def list_but_clicked(self):
        return
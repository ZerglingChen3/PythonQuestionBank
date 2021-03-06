from .surface import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from model import list as ls
import pandas as pd

global surface

choose_list = ["历史各类题目正确率",
               "本次各类题目正确率",
               "最近正确率统计",
               "最近做题数目统计",
               "历史各类题目比例"]

pro_list = ['单选题', '填空题', '简答题']


class userInformationChooseSurface(Surface):
    username = ""
    personLabel = ""
    nameSignal = pyqtSignal(str, str)
    nameSignal2 = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.information_widget, self.information_layout = getWidget()
        self.password_group_widget, self.password_group_layout = getGroup("修改密码")
        self.password_widget, self.password_layout = getWidget()
        self.password_button_widget, self.password_button_layout = getWidget()
        self.combobox_widget, self.combobox_layout = getWidget()
        self.data_group_widget, self.data_group_layout = getGroup("查看个人数据")
        self.prob_group_widget, self.prob_group_layout = getGroup("查看题目数据")

        self.password_label = QLabel("新密码：")
        self.password_text = QLineEdit()
        self.password_but = QPushButton("确认")

        self.list = QComboBox()
        self.list_but = QPushButton("确认")

        self.prob_list = QComboBox()
        self.num_text = QSpinBox()
        self.num_text.setMinimum(1)
        prob_cnt = len(ls.problem_list["单选题"]) + \
                   len(ls.problem_list["判断题"]) + \
                   len(ls.problem_list["简答题"])
        self.num_text.setMaximum(prob_cnt)
        self.pro_but = QPushButton("确认")
        self.pro_ans = QLabel("历史正确率:")

        self.logout_but = QPushButton("注销")
        self.back_but = QPushButton("返回")

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
        self.main_layout.addWidget(self.prob_group_widget, 6, 0, 3, 4)
        self.prob_group_layout.addWidget(self.prob_list, 0, 0)
        self.prob_group_layout.addWidget(self.num_text, 0, 1)
        self.prob_group_layout.addWidget(self.pro_but, 1, 0)
        self.prob_group_layout.addWidget(self.pro_ans, 2, 0)

    def initList(self):
        self.list.addItems(choose_list)
        self.prob_list.addItems(pro_list)

    def receive_nameSignal(self, name):
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.logout_but, 1, 0)
        self.information_layout.addWidget(self.back_but, 2, 0)
        self.main_layout.addWidget(self.information_widget, 1, 5, 3, 2)

    def initUI(self):
        self.resize(1080, 960)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

    def initEvent(self):
        self.logout_but.clicked.connect(self.logout_but_clicked)
        self.password_but.clicked.connect(self.password_but_clicked)
        self.list_but.clicked.connect(self.list_but_clicked)
        self.back_but.clicked.connect(self.back_but_clicked)
        self.pro_but.clicked.connect(self.pro_but_clicked)

    def pro_but_clicked(self):
        Type = self.prob_list.currentText()
        id = self.num_text.text()
        value = len(ls.problem_list[Type])
        if int(id) > value:
            QMessageBox.warning(self, '警告', "题目编号不合法，请重新输入！")
        data_path = "./data/user/"
        current_path = data_path + str(self.username)
        current_excel = current_path + "/data.xlsx"
        data = pd.read_excel(current_excel, sheet_name=Type)
        ans = 0
        for i in range(data.shape[0]):
            line = data.loc[i].values
            if int(line[0]) == int(id):
                ans = line[3]
                break
        self.pro_ans.setParent(None)
        self.pro_ans = QLabel('历史正确率为: {:.2%}'.format(ans))
        self.prob_group_layout.addWidget(self.pro_ans, 2, 0)

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
        choose = self.list.currentText()
        self.close()
        global surface
        surface = userInformationSurface()
        self.nameSignal.connect(surface.receive_nameSignal)
        self.nameSignal.emit(self.username, choose)
        surface.show()

    def back_but_clicked(self):
        self.close()
        global surface
        from gui import problem
        surface = problem.problemChooseSurface()
        self.nameSignal2.connect(surface.receive_nameSignal)
        self.nameSignal2.emit(self.username)
        surface.show()


class userInformationSurface(Surface):
    username = ""
    personLabel = ""
    choose = ""
    nameSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.information_widget, self.information_layout = getWidget()
        self.back_but = QPushButton("返回")

    def initPos(self):
        self.main_layout.addWidget(self.group_widget, 1, 0, 4, 4)

    def receive_nameSignal(self, name, choose):
        self.username = name
        self.choose = choose
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.back_but, 1, 0)
        self.group_widget, self.group_layout = getGroup(choose)
        self.main_layout.addWidget(self.information_widget, 1, 5, 2, 2)

        self.initPos()
        self.initFigure(choose)
        self.initUI()
        self.initEvent()

    def initFigure(self, choose):
        from model import figure
        self.F = figure.MyFigure(width=3, height=2, dpi=100)
        if choose == choose_list[0]:
            self.F.draw0()
        elif choose == choose_list[1]:
            self.F.draw1()
        elif choose == choose_list[2]:
            self.F.draw2(self.username)
        elif choose == choose_list[3]:
            self.F.draw3(self.username)
        elif choose == choose_list[4]:
            self.F.draw4(self.username)
        self.group_layout.addWidget(self.F)

    def initUI(self):
        self.resize(1080, 960)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

    def initEvent(self):
        self.back_but.clicked.connect(self.back_but_clicked)

    def back_but_clicked(self):
        self.close()
        global surface
        surface = userInformationChooseSurface()
        self.nameSignal.connect(surface.receive_nameSignal)
        self.nameSignal.emit(self.username)
        surface.show()

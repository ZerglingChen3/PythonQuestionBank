import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .surface import Surface
from model import list as ls
from model import problem as pr

# recode the surface
global surface


class problemChooseSurface(Surface):
    username = ""
    personLabel = ""
    nameSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.login_surface_widget = QWidget()
        self.login_surface_layout = QGridLayout()
        self.login_surface_widget.setLayout(self.login_surface_layout)

        self.button_widget = QWidget()
        self.button_layout = QGridLayout()
        self.button_widget.setLayout(self.button_layout)

        self.information_widget = QWidget()
        self.information_layout = QGridLayout()
        self.information_widget.setLayout(self.information_layout)

        self.headLabel = QLabel("题目选择")

        self.type_box_widget = QGroupBox("请选择题目类型")
        self.type_box_widget.setFlat(False)
        self.type_box_layout = QHBoxLayout()

        self.checkBox1 = QCheckBox("单选题")
        self.checkBox2 = QCheckBox("判断题")
        self.checkBox3 = QCheckBox("简答题")

        self.num_box_widget = QGroupBox("题目数量")
        self.num_box_layout = QHBoxLayout()

        self.num_text = QSpinBox()
        self.num_text.setMinimum(0)
        prob_cnt = len(ls.problem_list["单选题"]) + \
                   len(ls.problem_list["判断题"]) + \
                   len(ls.problem_list["简答题"])
        self.num_text.setMaximum(prob_cnt)

        self.reset_but = QPushButton("重置")
        self.ok_but = QPushButton("确定")
        self.logout_but = QPushButton("注销")

        self.initPos()
        self.initLabel()
        self.initEvent()
        self.initUI()

    def initPos(self):
        self.type_box_widget.setLayout(self.type_box_layout)
        self.type_box_layout.addWidget(self.checkBox1)
        self.type_box_layout.addWidget(self.checkBox2)
        self.type_box_layout.addWidget(self.checkBox3)

        self.num_box_widget.setLayout(self.num_box_layout)
        self.num_box_layout.addWidget(self.num_text)

        self.button_layout.addWidget(self.reset_but, 0, 0)
        self.button_layout.addWidget(self.ok_but, 0, 1)

        self.main_layout.addWidget(self.headLabel, 0, 0, 9, 9)
        self.main_layout.addWidget(self.type_box_widget, 2, 3, 2, 3)
        self.main_layout.addWidget(self.num_box_widget, 4, 3, 2, 3)
        self.main_layout.addWidget(self.button_widget, 6, 3, 1, 3)

    def initUI(self):
        self.resize(960, 720)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

    def initLabel(self):
        self.headLabel.setAlignment(Qt.AlignHCenter)
        self.headLabel.setStyleSheet("color:rgb(60,60,60,255);"
                                     "font-size:100px;"
                                     "font-weight:bold;"
                                     "font-family:Roman"
                                     "times;")
        self.headLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def initEvent(self):
        self.reset_but.clicked.connect(self.reset_but_clicked)
        self.ok_but.clicked.connect(self.ok_but_clicked)
        self.logout_but.clicked.connect(self.logout_but_clicked)

    def reset_but_clicked(self):
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.num_text.setValue(0)
        return

    def ok_but_clicked(self):
        choose1 = self.checkBox1.isChecked()
        choose2 = self.checkBox2.isChecked()
        choose3 = self.checkBox3.isChecked()
        value = self.num_text.value()
        if not choose1 and not choose2 and not choose3:
            QMessageBox.warning(self, '警告', "你没有选任何类型的题目！")
            return
        elif value == 0:
            QMessageBox.warning(self, '警告', "你没有选任何的题目！")
            return
        prob_cnt = choose1 * len(ls.problem_list["单选题"]) + \
                   choose2 * len(ls.problem_list["判断题"]) + \
                   choose3 * len(ls.problem_list["简答题"])

        if value > prob_cnt:
            QMessageBox.warning(self, '警告', "你选择的题目数量过多！")
            return

        print("#######################题目信息")
        ls.choose_problem_list.clear()
        if choose1:
            ls.choose_problem_list.extend(ls.problem_list["单选题"])
            print("我们有单选题~")
        if choose2:
            ls.choose_problem_list.extend(ls.problem_list["判断题"])
            print("我们有判断题~")
        if choose3:
            ls.choose_problem_list.extend(ls.problem_list["简答题"])
            print("我们有简答题~")
        random.shuffle(ls.choose_problem_list)
        ls.choose_problem_list = ls.choose_problem_list[0:value]
        print("我们的题目数量是：" + str(value))

        ls.choose_problem_show_list.clear()
        for i in range(len(ls.choose_problem_list)):
            pro = ls.choose_problem_list[i]
            problem_show = pr.problemShow(pro, i)
            ls.choose_problem_show_list.append(problem_show)


        global surface
        surface = problemSurface()
        self.nameSignal.connect(surface.receive_nameSignal)
        self.nameSignal.emit(self.username)
        surface.show()
        self.close()

    def logout_but_clicked(self):
        QMessageBox.information(self, '提醒', "欢迎您再使用小信题库！")
        from .login import loginSurface
        global surface
        surface = loginSurface()
        surface.show()
        self.close()

    def receive_nameSignal(self, name):
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.logout_but, 1, 0)
        self.main_layout.addWidget(self.information_widget, 1, 5, 1, 2)


class problemSurface(Surface):
    username = ""
    personLabel = ""

    def __init__(self):
        super().__init__()

        self.information_widget = QWidget()
        self.information_layout = QGridLayout()
        self.information_widget.setLayout(self.information_layout)

        self.headLabel = QLabel("")

        self.logout_but = QPushButton("注销")

        self.initPos()
        self.initUI()

    def initPos(self):
        self.main_layout.addWidget(self.headLabel, 0, 0, 100, 100)

        start = 0
        for i in range(len(ls.choose_problem_show_list)):
            pro_box = ls.choose_problem_show_list[i].getBoxWidget()
            self.main_layout.addWidget(pro_box, start, 0, 10, 6)
            start += 10

    def receive_nameSignal(self, name):
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.logout_but, 1, 0)
        self.main_layout.addWidget(self.information_widget, 0, 6, 2, 2)

    def initUI(self):
        self.resize(1440, 1080)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .surface import Surface
from model import list as ls
from model import problem as pr


# recode the surface
global surface

MAX_PROBLEM = 4


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
            print("有单选题!")
        if choose2:
            ls.choose_problem_list.extend(ls.problem_list["判断题"])
            print("有判断题!")
        if choose3:
            ls.choose_problem_list.extend(ls.problem_list["简答题"])
            print("有简答题!")
        random.shuffle(ls.choose_problem_list)
        ls.choose_problem_list = ls.choose_problem_list[0:value]
        print("题目数量是：" + str(value))

        ls.choose_problem_show_list.clear()
        for i in range(len(ls.choose_problem_list)):
            pro = ls.choose_problem_list[i]
            problem_show = pr.problemShow(pro, i)
            ls.choose_problem_show_list.append(problem_show)

        ls.choose_problem_surface_list.clear()
        i = 0
        while i < value:
            pro_list = []
            j = 0
            while i < value and j < MAX_PROBLEM:
                pro_list.append(ls.choose_problem_show_list[i])
                i += 1
                j += 1
            sf = problemSurface(pro_list)
            self.nameSignal.connect(sf.receive_nameSignal)
            ls.choose_problem_surface_list.append(sf)

        for i in range(len(ls.choose_problem_surface_list) - 1):
            ls.choose_problem_surface_list[i].linkFront(ls.choose_problem_surface_list[i + 1])

        for i in range(1, len(ls.choose_problem_surface_list)):
            ls.choose_problem_surface_list[i].linkBack(ls.choose_problem_surface_list[i - 1])

        self.nameSignal.emit(self.username)

        global surface
        surface = ls.choose_problem_surface_list[0]
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
    nameSignal = pyqtSignal(str)

    def __init__(self, pro_list):
        super().__init__()

        self.information_widget = QWidget()
        self.information_layout = QGridLayout()
        self.information_widget.setLayout(self.information_layout)

        self.headLabel = QLabel("")

        self.logout_but = QPushButton("注销")
        self.back_but = QPushButton("上一页")
        self.front_but = QPushButton("下一页")
        self.submit_but = QPushButton("提交")
        self.return_but = QPushButton("返回")
        self.user_but = QPushButton("个人信息")

        self.pro_list = pro_list

        self.front_surface = None
        self.back_surface = None

        self.button_widget = QWidget()
        self.button_layout = QGridLayout()
        self.button_widget.setLayout(self.button_layout)

        self.initPos()
        self.initUI()
        self.initEvent()

    def initPos(self):
        start = 0
        for i in range(len(self.pro_list)):
            pro_box = self.pro_list[i].getBoxWidget()
            self.main_layout.addWidget(pro_box, start, 0, 10, 6)
            start += 10
        self.button_layout.addWidget(self.back_but, 0, 0)
        self.button_layout.addWidget(self.front_but, 0, 1)
        self.button_layout.addWidget(self.submit_but, 0, 2)
        self.main_layout.addWidget(self.button_widget, start, 2)

    def receive_nameSignal(self, name):
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.information_layout.addWidget(self.logout_but, 1, 0)
        self.information_layout.addWidget(self.user_but, 2, 0)
        self.main_layout.addWidget(self.information_widget, 0, 6, 3, 2)

    def initEvent(self):
        self.back_but.clicked.connect(self.back_but_click)
        self.front_but.clicked.connect(self.front_but_click)
        self.logout_but.clicked.connect(self.logout_but_clicked)
        self.submit_but.clicked.connect(self.submit_but_clicked)
        self.return_but.clicked.connect(self.return_but_clicked)
        self.user_but.clicked.connect(self.user_but_clicked)

    def initUI(self):
        self.resize(1080, 960)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

    def linkFront(self, front_surface):
        self.front_surface = front_surface

    def linkBack(self, back_surface):
        self.back_surface = back_surface

    def front_but_click(self):
        if self.front_surface is None:
            QMessageBox.information(self, '提醒', "已经是最后一页！")
            return
        global surface
        surface = self.front_surface
        self.close()
        surface.show()

    def back_but_click(self):
        if self.back_surface is None:
            QMessageBox.information(self, '提醒', "已经是第一页！")
            return
        global surface
        surface = self.back_surface
        self.close()
        surface.show()

    def logout_but_clicked(self):
        from .login import loginSurface
        self.close()
        global surface
        surface = loginSurface()
        surface.show()

    def return_but_clicked(self):
        self.close()
        global surface
        surface = problemChooseSurface()
        self.nameSignal.connect(surface.receive_nameSignal)
        self.nameSignal.emit(self.username)
        surface.show()

    def user_but_clicked(self):
        self.close()
        from .user import userInformationChooseSurface
        global surface
        surface = userInformationChooseSurface()
        self.nameSignal.connect(surface.receive_nameSignal)
        self.nameSignal.emit(self.username)
        surface.show()

    def changeButton(self):
        self.submit_but.setParent(None)
        self.button_layout.addWidget(self.return_but, 0, 2)

    def submit_but_clicked(self):
        sum_short = 0  # the sum of short answer problem
        sum_tot = 0
        sum_correct = 0
        for pro in ls.choose_problem_show_list:
            state = "correct"
            if pro.getProType() == "简答题":
                sum_short += 1
                state = "can_not_judge"
            else:
                sum_tot += 1
                if pro.checkCorrect():
                    sum_correct += 1
                else:
                    state = "wrong"
            type_record = ls.problem_record[pro.getProType()]
            type_record.addRecord(pro.getId(), state)

        print("#######################答题情况")
        print("简答题数量：" + str(sum_short))
        print("非简答题数量：" + str(sum_tot))
        print("非简答题正确数量：" + str(sum_correct))
        self.close()

        for pro in ls.choose_problem_show_list:
            pro.resultShow()
        for sf in ls.choose_problem_surface_list:
            sf.changeButton()

        from manage import person as nps
        nps.appendProblemRecord(self.username)

        global surface
        surface = ls.choose_problem_surface_list[0]
        surface.show()

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .Surface import Surface

# recode the surface
global surface


class problemChooseSurface(Surface):
    username = ""
    personLabel = ""

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

        self.checkBox1 = QCheckBox("判断题")
        self.checkBox2 = QCheckBox("多选题")
        self.checkBox3 = QCheckBox("简答题")

        self.num_box_widget = QGroupBox("题目数量")
        self.num_box_layout = QHBoxLayout()

        self.num_text = QSpinBox()
        self.num_text.setMinimum(0)
        self.num_text.setMaximum(100)  # this need to read from the data base

        self.reset_but = QPushButton("重置")
        self.ok_but = QPushButton("确定")

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
        print("#######################题目信息")
        if choose1:
            print("我们有判断题~")
        if choose2:
            print("我们有多选题~")
        if choose3:
            print("我们有简答题~")
        print("我们的题目数量是：" + str(value))
        self.close()
        from .Login import loginSurface
        global surface
        surface = loginSurface()
        surface.show()

    def receive_nameSignal(self, name):
        # print("transform: " + str(name))
        self.username = name
        self.personLabel = QLabel("用户名：" + str(self.username))
        self.information_layout.addWidget(self.personLabel, 0, 0)
        self.main_layout.addWidget(self.information_widget, 1, 5, 1, 3)

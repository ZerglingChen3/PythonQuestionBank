from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .Surface import Surface


class problemChooseSurface(Surface):

    def __init__(self):
        super().__init__()

        self.login_surface_widget = QWidget()
        self.login_surface_layout = QGridLayout()
        self.login_surface_widget.setLayout(self.login_surface_layout)

        self.headLabel = QLabel("题目选择")
        self.personLabel = QLabel("用户名：")

        self.type_box_widget = QGroupBox("请选择题目类型")
        self.type_box_widget.setFlat(False)
        self.type_box_layout = QHBoxLayout()

        self.checkBox1 = QCheckBox("判断题")
        self.checkBox2 = QCheckBox("多选题")
        self.checkBox3 = QCheckBox("简答题")

        self.initPos()
        self.initUI()

    def initPos(self):
        self.type_box_widget.setLayout(self.type_box_layout)
        self.type_box_layout.addWidget(self.checkBox1)
        self.type_box_layout.addWidget(self.checkBox2)
        self.type_box_layout.addWidget(self.checkBox3)

        self.main_layout.addWidget(self.headLabel, 0, 0, 9, 9)
        self.main_layout.addWidget(self.type_box_widget, 3, 3, 2, 3)

    def initUI(self):
        self.resize(960, 720)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

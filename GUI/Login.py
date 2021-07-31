from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .surface import Surface
from .problem import problemChooseSurface
from model import list as ls
from model import person as ops
from manage import person as nps

# for test before data base
name_dict = {"admin": "19373469"}

# recode the surface
global surface


class loginSurface(Surface):
    nameSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.login_surface_widget = QWidget()
        self.login_surface_layout = QGridLayout()
        self.login_surface_widget.setLayout(self.login_surface_layout)

        self.login_button_widget = QWidget()
        self.login_button_layout = QGridLayout()
        self.login_button_widget.setLayout(self.login_button_layout)

        self.headLabel = QLabel("Python小信题库登录")
        self.unameLabel = QLabel("用户名：")
        self.pwdLabel = QLabel("  密码：")

        self.unameText = QLineEdit("admin")
        self.pwdText = QLineEdit("password")

        self.register_but = QPushButton("注册")
        self.login_but = QPushButton("登录")

        self.initLabel()
        self.initPos()
        self.initEvent()
        self.initUI()

    def initPos(self):
        self.main_layout.addWidget(self.headLabel, 0, 0, 9, 9)
        self.main_layout.addWidget(self.login_surface_widget, 3, 3, 2, 3)
        self.main_layout.addWidget(self.login_button_widget, 5, 3, 1, 3)
        self.login_surface_layout.addWidget(self.unameLabel, 0, 0)
        self.login_surface_layout.addWidget(self.unameText, 0, 1)
        self.login_surface_layout.addWidget(self.pwdLabel, 1, 0)
        self.login_surface_layout.addWidget(self.pwdText, 1, 1)
        self.login_button_layout.addWidget(self.register_but, 0, 0)
        self.login_button_layout.addWidget(self.login_but, 0, 1)

    def initLabel(self):
        self.headLabel.setAlignment(Qt.AlignHCenter)
        self.headLabel.setStyleSheet("color:rgb(60,60,60,255);"
                                     "font-size:100px;"
                                     "font-weight:bold;"
                                     "font-family:Roman"
                                     "times;")
        self.headLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.pwdText.setContextMenuPolicy(Qt.NoContextMenu)
        self.pwdText.setEchoMode(QLineEdit.Password)

    def initUI(self):
        self.resize(960, 720)
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))

    """
    when close, remind people whether he want to leave
    """

    def initEvent(self):
        self.login_but.clicked.connect(self.login_btn_clicked)
        self.register_but.clicked.connect(self.register_but_clicked)

    def login_btn_clicked(self):
        account = self.unameText.text()
        password = self.pwdText.text()

        if account == "":
            QMessageBox.warning(self, '警告', "用户名不能为空，请重新输入！")
            return
        elif password == "":
            QMessageBox.warning(self, '警告', "密码不能为空，请重新输入！")
            return
        else:  # 需要连接数据库
            find_person = False
            for user in ls.user_list:
                if str(user.getName()) == account:
                    find_person = True
                    if str(user.getPassword()) != password:
                        QMessageBox.warning(self, '警告', "用户名密码不匹配，请重新输入！")
                        return
                    if str(user.getPermission()) == "admin":
                        QMessageBox.information(self, '消息', "甜豆腐天下第一！")
                    else:
                        QMessageBox.information(self, '消息', "登录成功！")
                    break
            if not find_person:
                QMessageBox.warning(self, '警告', "用户名不存在，请重新输入！")
                return

        print("#######################登录信息")
        print("账户：  " + account)
        print("密码：  " + password)

        global surface
        surface = problemChooseSurface()

        nps.initData(account)
        self.nameSignal.connect(surface.receive_nameSignal)
        self.nameSignal.emit(account)
        surface.show()

        self.close()

    def register_but_clicked(self):
        self.close()
        global surface
        surface = registerSurface()
        surface.show()


class registerSurface(Surface):

    def __init__(self):
        super().__init__()

        self.register_surface_widget = QWidget()
        self.register_surface_layout = QGridLayout()
        self.register_surface_widget.setLayout(self.register_surface_layout)

        self.register_button_widget = QWidget()
        self.register_button_layout = QGridLayout()
        self.register_button_widget.setLayout(self.register_button_layout)

        self.headLabel = QLabel("注册")
        self.unameLabel = QLabel("用户名：")
        self.pwdLabel = QLabel("  密码：")
        self.re_pwdLabel = QLabel("确认密码：")

        self.unameText = QLineEdit("")
        self.pwdText = QLineEdit("")
        self.re_pwdText = QLineEdit("")

        self.back_but = QPushButton("返回")
        self.register_but = QPushButton("注册")

        self.initLabel()
        self.initPos()
        self.initEvent()
        self.initUI()

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

    def initPos(self):
        self.main_layout.addWidget(self.headLabel, 0, 0, 9, 9)
        self.main_layout.addWidget(self.register_surface_widget, 3, 3, 3, 3)
        self.main_layout.addWidget(self.register_button_widget, 6, 3, 1, 3)
        self.register_surface_layout.addWidget(self.unameLabel, 0, 0)
        self.register_surface_layout.addWidget(self.unameText, 0, 1)
        self.register_surface_layout.addWidget(self.pwdLabel, 1, 0)
        self.register_surface_layout.addWidget(self.pwdText, 1, 1)
        self.register_surface_layout.addWidget(self.re_pwdLabel, 2, 0)
        self.register_surface_layout.addWidget(self.re_pwdText, 2, 1)
        self.register_button_layout.addWidget(self.back_but, 0, 0)
        self.register_button_layout.addWidget(self.register_but, 0, 1)

    def initEvent(self):
        self.back_but.clicked.connect(self.back_but_clicked)
        self.register_but.clicked.connect(self.register_but_clicked)

    def back_but_clicked(self):
        self.close()
        global surface
        surface = loginSurface()
        surface.show()

    def register_but_clicked(self):
        account = self.unameText.text()
        password = self.pwdText.text()
        password_again = self.re_pwdText.text()

        if account == "":
            QMessageBox.warning(self, '警告', "用户名不能为空，请重新输入！")
            return
        elif password == "":
            QMessageBox.warning(self, '警告', "密码不能为空，请重新输入！")
            return
        elif password != password_again:
            QMessageBox.warning(self, '警告', "确认密码不正确，请重新输入！")
            return
        else:
            for user in ls.user_list:
                if str(user.getName()) == account:
                    QMessageBox.warning(self, '警告', "用户名已经使用，请重新输入！")
                    return
            user = ops.person(account, password, "user")
            nps.appendPerson(user)
            QMessageBox.information(self, '消息', "注册成功!")

        global surface
        surface = loginSurface()
        surface.show()
        self.close()
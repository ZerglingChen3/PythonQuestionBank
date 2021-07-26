from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(10)
        self.main_widget.setLayout(self.main_layout)

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
        # self.use_palette()
        self.initPlace()
        self.initUI()

    def initPlace(self):
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
        self.headLabel.setStyleSheet("color:rgb(40,40,255,255);"
                                     "font-size:150px;"
                                     "font-weight:bold;"
                                     "font-family:Roman"
                                     "times;")
        self.headLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.main_layout.addWidget(self.headLabel, 0, 0, 4, 10)

        self.pwdText.setContextMenuPolicy(Qt.NoContextMenu)

        '''
        # self.layout.addWidget(self.none, 2, 0, 1, 4)
        self.layout.addWidget(self.unameLabel, 2, 4, 1, 1)
        self.layout.addWidget(self.unameText, 2, 5, 1, 1)
        self.layout.addWidget(self.unameLabel, 2, 7, 1, 1)
        # self.layout.addWidget(self.none, 2, 7, 1, 3)
        self.layout.addWidget(self.pwdLabel, 3, 4, 1, 1)
        self.layout.addWidget(self.pwdText, 3, 5, 1, 1)
        self.layout.addWidget(self.register_but, 4, 4, 1, 1)
        self.layout.addWidget(self.login_but, 4, 5, 1, 1)
        '''

    def initUI(self):
        self.setLayout(self.main_layout)
        self.resize(1080, 960)
        self.center()
        self.setWindowTitle('小信题库')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))
        self.show()

    """
    when close, remind people whether he want to leave
    """

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提醒',
                                     "你确定要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    """
    set the windows into the middle
    """

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    '''
    when press the key, event happened
    '''

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def use_palette(self):
        """
        window_pale = QPalette()
        pixmap = QBrush(QPixmap("./pictures/shixiaoxin.jpg").
                        scaled(self.width(), self.height()))

        window_pale.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(window_pale)
        """

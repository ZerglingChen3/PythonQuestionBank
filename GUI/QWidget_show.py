from PyQt5.QtWidgets import (QWidget, QMessageBox, QDesktopWidget,
                             QApplication, QGridLayout, QLabel,
                             QSizePolicy, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.headLabel = QLabel("Python小信题库登录")
        self.unameLabel = QLabel("用户名：")
        self.pwdLabel = QLabel("  密码：")
        self.unameText = QLineEdit()
        self.pwdText = QLineEdit()
        self.initLabel()
        self.initUI()

    def initLabel(self):
        self.headLabel.setAlignment(Qt.AlignHCenter)
        self.headLabel.setStyleSheet("color:rgb(40,40,255,255);"
                                     "font-size:150px;"
                                     "font-weight:bold;"
                                     "font-family:Roman"
                                     "times;")
        self.headLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.pwdText.setContextMenuPolicy(Qt.NoContextMenu)

        self.unameText.setText("admin")
        self.pwdText.setText("password")

        self.layout.addWidget(self.headLabel, 0, 0, 5, 2)
        self.layout.addWidget(self.unameLabel, 1, 0)
        self.layout.addWidget(self.unameText, 1, 1)
        self.layout.addWidget(self.pwdLabel, 2, 0)
        self.layout.addWidget(self.pwdText, 2, 1)

    def initUI(self):
        self.layout.setSpacing(10)
        self.setLayout(self.layout)
        self.resize(2000, 1000)
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
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Surface(QWidget):

    def __init__(self):
        super().__init__()
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(10)
        self.main_widget.setLayout(self.main_layout)
        self.setLayout(self.main_layout)
        self.center()
        self.paintEvent(self)
        # self.use_palette()

    """
    when close, remind people whether he want to leave
    """

    '''
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提醒',
                                     "你确定要退出吗？", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    '''

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

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./pictures/login.jfif")
        painter.drawPixmap(self.rect(), pixmap)

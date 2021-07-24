from PyQt5.QtWidgets import (QWidget, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(2000, 1000)
        self.center()
        self.setWindowTitle('Test')
        self.setWindowIcon(QIcon('./pictures/shixiaoxin.jpg'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
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

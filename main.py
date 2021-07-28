import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

from gui import login
from manage import initdata

if __name__ == '__main__':
    initdata.init()
    ex = login.loginSurface()
    ex.show()
    app.exec_()

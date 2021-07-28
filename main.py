import sys
from PyQt5.QtWidgets import QApplication
from gui import login
from manage import initdata

if __name__ == '__main__':
    initdata.user_init()
    app = QApplication(sys.argv)
    ex = login.loginSurface()
    ex.show()
    app.exec_()

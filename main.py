import sys
from PyQt5.QtWidgets import QApplication
from GUI import login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = login.loginSurface()
    ex.show()
    app.exec_()

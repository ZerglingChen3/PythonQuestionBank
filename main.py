import sys
from PyQt5.QtWidgets import QApplication
from GUI import Login
from GUI import QWindows_show

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login.loginSurface()
    ex.show()
    app.exec_()
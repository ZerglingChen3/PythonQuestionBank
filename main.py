import sys
from PyQt5.QtWidgets import QApplication
from GUI import Login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login.loginSurface()
    ex.show()
    app.exec_()

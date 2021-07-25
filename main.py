import sys
from PyQt5.QtWidgets import QApplication
from GUI import QWidget_show
from GUI import QWindows_show

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QWidget_show.Example()
    # ex = QWindows_show.Example()

    sys.exit(app.exec_())

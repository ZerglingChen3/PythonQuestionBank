from PyQt5.QtWidgets import *


class problem:

    def __init__(self, line, type):
        self.__option = []
        self.__id = line[0]
        self.__description = line[1]
        self.__option.append(line[2])
        self.__option.append(line[3])
        self.__option.append(line[4])
        self.__option.append(line[5])
        self.__ans = line[6]
        self.__solve = line[7]
        self.__type = type

    def getType(self):
        return self.__type

    def getDes(self):
        return self.__description

    def getOpt(self, num):
        return str(self.__option[num])


class problemShow:

    def __init__(self, pro, pro_id):
        self.__box_widget = QGroupBox()
        self.__box_layout = QVBoxLayout()
        self.__option = {}
        self.__box_widget.setLayout(self.__box_layout)
        self.__descriptionLabel = QLabel(str(pro_id+1) + '.' + str(pro.getDes()))
        self.__box_layout.addWidget(self.__descriptionLabel, 0)
        if pro.getType() == "单选题":
            for num in range(ord('A'), ord('E')):
                ch = chr(num)
                widget = QRadioButton(ch + '. ' + pro.getOpt(num - ord('A')))
                self.__option[ch] = widget
                self.__box_layout.addWidget(widget, num + 1 - ord('A'))

    def getBoxWidget(self):
        return self.__box_widget

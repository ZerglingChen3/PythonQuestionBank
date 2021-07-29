from PyQt5.QtWidgets import *


def setColor(widget, color):
    widget.setStyleSheet("color:"+str(color))


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

    def getAns(self):
        return str(self.__ans)


class problemShow:

    def __init__(self, pro, pro_id):
        self.__problem = pro
        self.__box_widget = QGroupBox(pro.getType())
        self.__box_layout = QVBoxLayout()
        self.__option = {}
        self.__box_widget.setLayout(self.__box_layout)
        self.__descriptionLabel = QLabel(str(pro_id + 1) + '.' + str(pro.getDes()))
        self.__box_layout.addWidget(self.__descriptionLabel, 0)
        if pro.getType() == "单选题":
            for num in range(ord('A'), ord('E')):
                ch = chr(num)
                widget = QRadioButton(ch + '. ' + pro.getOpt(num - ord('A')))
                self.__option[ch] = widget
                self.__box_layout.addWidget(widget, num + 1 - ord('A'))
        elif pro.getType() == "判断题":
            widget_true = QRadioButton("正确")
            widget_false = QRadioButton("错误")
            self.__option["A"] = widget_true
            self.__option["B"] = widget_false
            self.__box_layout.addWidget(widget_true, 0)
            self.__box_layout.addWidget(widget_false, 1)
        elif pro.getType() == "简答题":
            widget_text = QTextEdit("")
            self.__option["A"] = widget_text
            self.__box_layout.addWidget(widget_text, 0)

    def getBoxWidget(self):
        return self.__box_widget

    def getProType(self):
        return str(self.__problem.getType())

    def checkCorrect(self):
        if self.__problem.getType() == "单选题" or self.__problem.getType() == "判断题":
            widget_target = self.__option[self.__problem.getAns()]
            if widget_target.isChecked():
                return True
            else:
                return False
        elif self.__problem.getType() == "简答题":
            print("简答题不可以判断正误！")
            exit(-1)

    def resultShow(self):
        if self.__problem.getType() == "单选题":
            for num in range(ord('A'), ord('E')):
                ch = chr(num)
                self.__option[ch].setParent(None)
                text = QLabel(ch + '. ' + self.__problem.getOpt(num - ord('A')))
                if self.__option[ch].isChecked():
                    if self.__problem.getAns() == ch:
                        setColor(text, "green")
                    else:
                        setColor(text, "red")
                elif self.__problem.getAns() == ch:
                    setColor(text, "green")
                self.__box_layout.addWidget(text, num + 1 - ord('A'))
        elif self.__problem.getType() == "判断题":
            for num in range(ord('A'), ord('C')):
                ch = chr(num)
                self.__option[ch].setParent(None)
                text = QLabel(ch + '. ' + self.__problem.getOpt(num - ord('A')))
                if self.__option[ch].isChecked():
                    if self.__problem.getAns() == ch:
                        setColor(text, "green")
                    else:
                        setColor(text, "red")
                elif self.__problem.getAns() == ch:
                    setColor(text, "green")
                self.__box_layout.addWidget(text, num + 1 - ord('A'))
        elif self.__problem.getType() == "简答题":
            self.__option["A"].setParent(None)
            you_answer = QLabel("你的答案：" + str(self.__option["A"].toPlainText()))
            correct_answer = QLabel("标准答案：" + str(self.__problem.getAns()))
            self.__box_layout.addWidget(you_answer, 1)
            self.__box_layout.addWidget(correct_answer, 2)

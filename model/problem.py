from PyQt5.QtWidgets import *


def setColor(widget, color):
    widget.setStyleSheet("color:" + str(color))


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

    def getId(self):
        return self.__id

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

    def getId(self):
        return self.__problem.getId()

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


class problemRecord:

    def __init__(self, pro_type, line):
        self.__type = pro_type
        self.__id = line[0]
        self.__time = line[1]
        self.__correct = line[2]
        self.__rate = line[3]

    def getId(self):
        return str(self.__id)

    def addRecord(self, state):
        self.__time += 1
        if state == "correct":
            self.__correct += 1
        self.__rate = self.__correct / self.__time

    def getFrame(self):
        return [self.__id, self.__time, self.__correct, self.__rate]


class typeRecord:

    def __init__(self, pro_type):
        self.__record = []
        self.__type = pro_type

    def initRecord(self, line):
        pro = problemRecord(self.__type, line)
        self.__record.append(pro)

    def addRecord(self, pro_id, state):
        for pro in self.__record:
            if pro.getId() == str(pro_id):
                pro.addRecord(state)
                return
        line = [pro_id, 0, 0, 0]
        pro = problemRecord(self.__type, line)
        self.__record.append(pro)
        pro.addRecord(state)

    def getType(self):
        return self.__type

    def getFrame(self):
        from manage import person as ps
        frame = {}
        for head in ps.problem_record_list:
            frame[head] = []
        for pro in self.__record:
            pro_frame = pro.getFrame()
            for j in range(4):
                frame[ps.problem_record_list[j]].append(pro_frame[j])
        return frame

import os
from model import list as ls
from manage import initdata as init
from model import problem as pb
import pandas as pd

problem_type = ["单选题", "判断题", "简答题"]

global problem_record_list
problem_record_list = ["题号", "答题次数", "错误次数", "错误率"]


def appendPerson(new_person):
    df = pd.read_excel(init.user_path)
    ls.user_list.append(new_person)
    ds = pd.DataFrame({"序号": [str(len(ls.user_list))],
                       "姓名": [new_person.getName()],
                       "密码": [new_person.getPassword()],
                       "权限": [new_person.getPermission()]})
    df = df.append(ds)
    df.to_excel(init.user_path, index=False, header=True)


data_path = "./data/user/"


def appendProblemRecord(name):
    current_path = data_path + str(name)
    current_excel = current_path + "/data.xlsx"
    writer = pd.ExcelWriter(current_excel)
    for type_record in problem_type:
        frame = ls.problem_record[type_record].getFrame()
        ds = pd.DataFrame(frame)
        ds.to_excel(writer, sheet_name=type_record, index=False)

    writer.save()
    writer.close()


def initDirectory(name):
    current_path = data_path + str(name)
    if not os.path.exists(current_path):
        os.mkdir(current_path)


def initExcel(name):
    current_path = data_path + str(name)
    current_excel = current_path + "/data.xlsx"
    if not os.path.exists(current_excel):
        writer = pd.ExcelWriter(current_excel)
        for pro_type in problem_type:
            ds = pd.DataFrame({"题号": [],
                               "答题次数": [],
                               "错误次数": [],
                               "错误率": []})
            ds.to_excel(writer, sheet_name=pro_type, index=False)
        writer.save()
        writer.close()

    ls.problem_record.clear()
    for pro_type in problem_type:
        type_record = pb.typeRecord(pro_type)
        ls.problem_record[pro_type] = type_record
        sheet = pd.read_excel(current_excel, sheet_name=pro_type)
        problem_cnt = sheet.shape[0]
        for i in range(problem_cnt):
            line = sheet.loc[i].values
            type_record.initRecord(line)


def initData(name):
    initDirectory(name)
    initExcel(name)

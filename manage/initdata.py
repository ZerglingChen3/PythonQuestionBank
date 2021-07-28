import os
import pandas as pd
from model import list as ls
from model import person

global user_path
user_path = "./data/user.xlsx"
global problem_path
problem_path = "./data/problem.xlsx"


def user_init():
    global user_path
    if not os.path.exists(user_path):
        df = pd.DataFrame({"序号": {}, "姓名": {}, "密码": {}, "权限": {}})
        df.to_excel(user_path, index=False)
    data = pd.read_excel(user_path)

    person_cnt = data.shape[0]

    for i in range(person_cnt):
        line = data.loc[i].values
        name = line[1]
        password = line[2]
        permission = line[3]
        user = person.person(name, password, permission)
        ls.user_list.append(user)

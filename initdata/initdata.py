import os
import pandas as pd

global user_path
user_path = "./data/user.xlsx"
global problem_path
problem_path = "./data/problem.xlsx"

global user_list
user_list = []
global problem_list
problem_list = []


def user_init():
    global user_path
    if not os.path.exists(user_path):
        df = pd.DataFrame({"序号": {}, "姓名": {}, "密码": {}})
        df.to_excel(user_path, index=False)
    data = pd.read_excel(user_path)
    print(data)

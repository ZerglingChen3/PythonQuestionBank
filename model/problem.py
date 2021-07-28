import pandas as pd


class problem:
    __description = ""
    __id = 0
    __type = ""
    __option = []
    __ans = ""
    __solve = ""

    def __init__(self, file, sheet_name, row):
        data = pd.read_excel(file, sheet_name=sheet_name).ix[row]
        print(data)


class person:
    __username = ""
    __password = ""

    def __init__(self, username, password):
        __username = username
        __password = password


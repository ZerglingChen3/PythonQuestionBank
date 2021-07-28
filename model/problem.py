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

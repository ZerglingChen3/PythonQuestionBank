import pandas as pd


class problem:
    __description = ""
    __id = 0
    __type = ""
    __option = []
    __ans = ""
    __solve = ""

    def __init__(self, line, type):
        self.__id = line[0]
        self.__description = line[1]
        self.__option.append(line[2])
        self.__option.append(line[3])
        self.__option.append(line[4])
        self.__option.append(line[5])
        self.__ans = line[6]
        self.__solve = line[7]
        self.__type = type

class person:

    def __init__(self, username, password, permission):
        self.__username = username
        self.__password = password
        self.__permission = permission

    def getName(self):
        return self.__username

    def getPermission(self):
        return self.__permission

    def getPassword(self):
        return self.__password

    def changePassword(self, password):
        self.__password = password


import os
import hashlib
class UserControl:
    """this class control users log-in activity"""
    def __init__(self):
        self.login = ""
        self.password = ""
        self.filePath = "../../pass.vkm"
        self.hashPassword = ""

    def __requestData(self):
        self.login = input("Hello, enter login please\n")
        self.password = input("and password\n")
        self.__saveData()

    def __showData(self):
        print("Login of current user: "+self.login+"\n")
        print("Password of current user: "+self.password+"\n")
        self.__hashPass()
        print("Hash password of current user: "+self.hashPassword+"\n")

    def __saveData(self):
        f = open(self.filePath, "w")
        f.write(self.login+"\n"+self.password)
        f.close()
        print("Password saved")

    def loadData(self):
        if(os.path.isfile(self.filePath)):
            f = open(self.filePath, "r")
            self.login = f.readline()
            self.password = f.readline()
            f.close()
        else:
            self.__requestData()
            print("Create new file pass.vkm")
        self.__showData()

    def __hashPass(self):
        self.hashPassword = hashlib.md5(self.password.encode()).hexdigest()
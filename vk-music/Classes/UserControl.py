class UserControl:
    """this class control users log-in activity"""
    def __init__(self):
        login = ""
        password = ""
    def requestData(self):
        self.login = input("Hello, enter login please\n")
        self.password = input("and password\n")
    def showData(self):
        print("Login of current user: "+self.login+"\n")
        print("Password of current user: "+self.password+"\n")
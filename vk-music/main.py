import vk
from random import randint
from Classes.UserController import userController
from Classes.vkAppController import vkAppController
from Classes.audioController import audioController

userController = userController()
userController.loadData()

vkApp = vkAppController()
vkapi = vk.API(vkApp.appId, userController.login, userController.password)
vkapi.scope = vkApp.scopes
accessToken = vkapi.get_access_token()#need for scope

profiles = vkapi.users.get()
print(profiles[0]['first_name']+' '+profiles[0]['last_name'])
audiocontroll = audioController()
audiocontroll.audioTaker()
print (audiocontroll)


"""key = input("Do you wanna change account?, y/n")
if (key == "y"):
    userController.__requestData(self)
else:
    input("GG, wp")"""



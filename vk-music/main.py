import vk
from random import randint
from Classes.UserController import userController
from Classes.vkAppController import vkAppController


userController = userController()
userController.loadData()

vkApp = vkAppController()
vkapi = vk.API(vkApp.appId, userController.login, userController.password)
vkapi.scope = vkApp.scopes
accessToken = vkapi.get_access_token()#need for scope

profiles = vkapi.users.get()
print(profiles[0]['first_name']+' '+profiles[0]['last_name'])
#debug msg:
debug = randint(0,100)
debug = str(debug)
vkapi('status.set', text = 'debug msg ' + debug)
import vk
from random import randint
from Classes.UserControl import UserControl


userControl = UserControl()
userControl.loadData()
vkapi = vk.API('4623020', userControl.login, userControl.password)
vkapi.scope = "friends"
xop = vkapi.get_access_token()#need for scope
profiles = vkapi.users.get(user_id=74487517)
print(profiles[0]['first_name']+' '+profiles[0]['last_name'])
#debug msg:
debug = randint(0,100)
debug = str(debug)
vkapi('status.set', text = 'debug msg ' + debug)
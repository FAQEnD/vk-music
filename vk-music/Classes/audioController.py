import vk

class audioController():
  """this class controlls audio information"""
  def _init_(self):
      #self.countAudio = 6000
      self.artist = ""
      self.title = ""
      self.urlDownload = ""
      self.duration = ""
  def audioTaker (self):
      vkapi = vk.API(vkApp.appId, userController.login, userController.password)
      vkapi('audio.get', count = 6000)
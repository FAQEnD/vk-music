import vk
import sys
import urllib

class audioController():
  """this class controlls audio information"""
  def __init__(self):
      self.countAudio = 5
      self.artist = []
      self.title = []
      self.downloadURL = []
      self.duration = []
      self.musicDir = "E:/FAQEnD/Music/" #Your music dir
      self.fullFileDir = []

  def getAudio(self, vkapi):
      audio = vkapi('audio.get', count = self.countAudio, need_user = 0)
      bannedChar = {':', '\\', '/', '*', '\"', '<', '>', '|', '?'}
      i = 0
      #print(audio)
      while i < len(audio['items']):
        self.artist.append(audio['items'][i]['artist'])
        self.title.append(audio['items'][i]['title'])
        self.duration.append(audio['items'][i]['duration'])
        self.downloadURL.append(audio['items'][i]['url'])
        #str = str.encode(sys.stdout.encoding, errors='replace')
        for badChar in bannedChar:
            if badChar in self.artist[i]:
                self.artist[i] = self.artist[i].replace(badChar, '')
            if badChar in self.title[i]:
                self.title[i] = self.title[i].replace(badChar, '')

        self.fullFileDir.append(self.musicDir + self.artist[i] + ' - ' + self.title[i] + '.mp3')
        try:
            print(self.fullFileDir[i], end = '')
        except UnicodeEncodeError as inst:
            for ch in self.fullFileDir[i]:
                try:
                    print(ch, end = '')
                except UnicodeEncodeError:
                    print('', end = '')
        print('');
        self.downloadFile(i)
        i += 1

  def downloadFile(self, fileIndex):
      mp3file = urllib.request.urlopen(self.downloadURL[fileIndex])
      output = open(self.fullFileDir[fileIndex], 'wb')
      output.write(mp3file.read())
      output.close()
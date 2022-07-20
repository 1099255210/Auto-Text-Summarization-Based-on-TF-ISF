from typing import List

class File_data:

  def __init__(self, filename:str, content:str):
    self.filename = filename
    self.content = content


class Folder_data:

  def __init__(self, foldername:str):
    self.filelist:List[File_data] = []
    self.foldername = foldername
    self.filenumber = 0

  def append(self, file:File_data):
    self.filelist.append(file)
    self.filenumber += 1


class Data:

  def __init__(self):
    self.folderlist:List[Folder_data] = []
    self.foldernumber = 0

  def append(self, folder:Folder_data):
    self.folderlist.append(folder)
    self.foldernumber += 1


class Sentense:

  def __init__(self):
    self.content = ''
    self.wordsnumber = 0
    self.wordlist = []
    self.originwordlist = []

  def inputSen(self, content:str, words:List[str]):
    self.content = content
    self.wordsnumber = len(words)
    self.wordlist = words
    
  def inputOriginalWordlist(self, wordlist:List[str]):
    self.originwordlist = wordlist

  def getWordTimes(self, word:str):
    return self.wordlist.count(word)
  
  def getWordlist(self):
    return self.wordlist
  
  def getOriginWordList(self):
    return self.originwordlist


class SentenseSet:

  def __init__(self):
    self.sentenselist:List[Sentense] = []
    self.sentensenumber = 0

  def add(self, sentense:Sentense):
    self.sentenselist.append(sentense)
    self.sentensenumber += 1

  def getWordTimes(self, word:str):
    wordtime = 0
    for sentense in self.sentenselist:
      if sentense.wordlist.count(word):
        wordtime += 1
    return wordtime
  
  def getWordlist(self):
    wordlist = []
    for sentense in self.sentenselist:
      wordlist.append(sentense.wordlist)
    return wordlist
  
  def getOriginWordlist(self):
    wordlist = []
    for sentense in self.sentenselist:
      wordlist.append(sentense.originwordlist)
    return wordlist


class FileStat:

  def __init__(self):
    self.words:List[Word] = []
    self.total = 0
    self.content = ''
    self.sentenselist = []
    self.filename = ''

  def inputFile(self, file:File_data):
    self.filename = file.filename
    self.content = file.content


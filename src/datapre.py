from cgitb import reset
import sys
import re
from typing import List
import datadef
import porterstemming
from nltk.corpus import stopwords
import nltk.data

PS = porterstemming.PorterStemmer()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

replace_sig = ["''", "``", ".", ",", "\n"]

def prepare_new(folder_data:datadef.Folder_data) -> datadef.SentenseSet:
  retset = datadef.SentenseSet()
  
  for file in folder_data.filelist:

    filestat = datadef.FileStat()
    filestat.inputFile(file)
    filestat.sentenselist = tokenizer.tokenize(file.content)

    for sen in filestat.sentenselist:
      sentense = datadef.Sentense()
      inputwords = []
      originwords = []

      content = sen

      for sig in replace_sig:
        content = content.replace(sig, "")  # replace all the useless marks
      wordlist = content.split(' ')         # get a word list

      for word in wordlist:
        word = re.sub("[^A-Za-z]+", ' ', str(word)).lower().strip()
        if word == '':
          continue
        if word in stopwords.words('english'):  # get rid of stop words
          continue
        originwords.append(word)
        word = PS.stem(word, 0, len(word) - 1)  # get the root of the word
        inputwords.append(word)

      if inputwords == []:
        continue
      sentense.inputOriginalWordlist(originwords)
      sentense.inputSen(sen, inputwords)
      retset.add(sentense)
  
  return retset


def prepareBaseline(data:datadef.Data) -> dict:
  
  retdict = {}
  
  for folder in data.folderlist:
    summary = ''
    for file in folder.filelist:
      summary += tokenizer.tokenize(file.content)[0]
      if sys.getsizeof(summary) > 665:
        break
    retdict[folder.foldername + '.txt'] = summary
  
  return retdict

      
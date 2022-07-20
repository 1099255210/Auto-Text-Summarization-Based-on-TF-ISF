import datadef
import os
from typing import List

defaultpath = './大作业/docs/'
# defaultpath = '../docs/'
defaultrespath = './大作业/sum/'
defaultpartpath = './大作业/partresult/'

def get_data(path=defaultpath) -> datadef.Data:
  data = datadef.Data()
  for folder in os.listdir(path=path):
    nextpath = path
    if path[-1] != '/':
      nextpath += '/'
    nextpath += folder + '/'

    folder_data = datadef.Folder_data(folder.split('/')[-1])

    for file in os.listdir(path=nextpath):
      filepath = nextpath + file
      with open(file=filepath, mode='r', encoding='utf-8') as fp:
        content = fp.read()
        content = content.split('<TEXT>')[-1]
        content = content.split('<')[0]
        file_data = datadef.File_data(filename=file, content=content)
        folder_data.append(file_data)
        
    data.append(folder=folder_data)

  return data

def get_resultfile(path=defaultrespath) -> dict:
  
  retdict = {}
  for file in os.listdir(path=path):
    filepath = path + file
    with open(file=filepath, mode='r', encoding='utf-8') as fp:
      content = fp.read()
      retdict[file] = content
      
  return retdict
  
def get_partresult(resultfile:dict) -> dict:
  retdict = {}
  
  for i in range(len(resultfile)):
    name = str(list(resultfile)[i])
    name = name.upper()
    name = name.split('T')[0]
    
    contentlist = []
    for file in os.listdir(path=defaultpartpath):
      
      if file.startswith(name):
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for alp in alpha:
          if file.endswith(alp):
            with open(file=defaultpartpath + file, mode='r', encoding='utf-8') as fp:
              content = fp.read()
              contentlist.append(content)
            
    retdict[str(list(resultfile)[i])] = contentlist

  return retdict
    
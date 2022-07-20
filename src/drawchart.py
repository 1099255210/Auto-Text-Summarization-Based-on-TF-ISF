import numpy as np
import matplotlib.pyplot as plt
import json

def drawChart(type:str):
  
  myres = []
  with open('./大作业/result.json', 'r', encoding='utf-8') as fp:
    result = json.loads(fp.read()) 
    for item in result:
      value = result[item][type]['r']
      myres.append(value)
      
  baseres = []
  with open('./大作业/result_baseline.json', 'r', encoding='utf-8') as fp:
    result = json.loads(fp.read())
    for item in result:
      value = result[item][type]['r']
      baseres.append(value)
      
  myresarr = np.array(myres)
  baseresarr = np.array(baseres)
  
  plt.figure(figsize=(15,4))
  plt.title(type)
  b1 = plt.bar(range(50), myresarr, color='#FF000044')
  b2 = plt.bar(range(50), baseresarr, color='#0000FF44')
  plt.legend(handles=[b1, b2], labels=['myresult', 'baseline'], loc='best')
  plt.savefig('./大作业/img/sen2vec/' + type + '.png')
  plt.show()

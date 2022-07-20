import numpy
import datadef
import sys
import similarity
from typing import List

def generateSum_new(similarvalue:dict, senset:datadef.SentenseSet, tfisfarr:numpy.ndarray, folder:str) -> str:

  summary = ''
  selected = []

  simvaluedict = similarvalue
  sentenseset = senset
  topicname = folder
  
  for i in range(len(simvaluedict)):
    index = simvaluedict[i][0]
    
    appendcontent = sentenseset.sentenselist[index].content.replace('\n', '')
    
    # get rid of sentenses that are similar to selected sentenses.
    mainvec = tfisfarr[index]
    for j in range(len(selected)):
      selvec = tfisfarr[j]
      if similarity.calSimilarity(mainvec, selvec) > 0.9:
        appendcontent = ''
        break
    
    summary += appendcontent
    selected.append(index)
    
    if sys.getsizeof(summary) > 665:
      break
  print('topic:' + topicname)
  print('summary:')
  print(summary)
  print('----------------------------------------')
  
  return summary
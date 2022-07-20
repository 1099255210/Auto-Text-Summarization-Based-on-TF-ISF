import math
import numpy
import datadef
from typing import List

def getTFISF_new(senset:datadef.SentenseSet) -> numpy.ndarray:
  wordlist = []

  for sentense in senset.sentenselist:
    for word in sentense.wordlist:
      if word not in wordlist:
        wordlist.append(word)
  
  tfisf = []

  for word in wordlist:

    isf = math.log(
      senset.sentensenumber / (senset.getWordTimes(word) + 1)
    )

    rowvalue = []
    allwordnumber = 0
    allwordtime = 0

    for sentense in senset.sentenselist:

      tf = sentense.getWordTimes(word) / sentense.wordsnumber
      rowvalue.append(tf * isf)

      # for allsen stat
      allwordnumber += sentense.wordsnumber
      allwordtime += sentense.getWordTimes(word)
    
    # for allsen stat
    alltf = allwordtime / allwordnumber
    rowvalue.append(alltf * isf)

    tfisf.append(rowvalue)

  tfisf_arr = numpy.array(tfisf)
  tfisf_arr = tfisf_arr.transpose()
  return tfisf_arr

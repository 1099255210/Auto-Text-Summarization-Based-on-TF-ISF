import numpy
from typing import List

def getSimilarityArr_new(tfisfarr:numpy.ndarray):
  
  simvaluedict = {}
  allsen = tfisfarr[-1]
  for i in range(len(tfisfarr) - 1):
    simv = calSimilarity(allsen, tfisfarr[i])
    simvaluedict[i] = simv

  simvaluedict = sorted(simvaluedict.items(), key=lambda item: item[1], reverse=True)

  return simvaluedict


def calSimilarity(arr1:numpy.ndarray, arr2:numpy.ndarray):
  retval = numpy.dot(arr1, arr2) / (numpy.linalg.norm(arr1) * numpy.linalg.norm(arr2))
  return retval
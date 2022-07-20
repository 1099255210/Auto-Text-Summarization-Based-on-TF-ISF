from rouge import Rouge

def compare(myresult:dict, partresult:dict) -> dict:
  
  retdict = {}
  
  rouge = Rouge()
  for key in myresult.keys():
    suma = myresult[key]
    sumb = partresult[key]
    
    maxv = 0
    maxind = 0
    for item in sumb:
      scores = rouge.get_scores(suma, item)
      if scores[0]['rouge-1']['r'] > maxv:
        maxv = scores[0]['rouge-1']['r']
        maxind = sumb.index(item)
    
    scores = rouge.get_scores(suma, sumb[maxind])
  
    retdict[key] = scores[0]
    
  return retdict

def compareBaseline(baselineresult:dict, partresult:dict) -> dict:
  
  retdict = {}
  
  rouge = Rouge()
  for key in baselineresult.keys():
    suma = baselineresult[key]
    sumb = partresult[key]
    
    scores = rouge.get_scores(suma, sumb[0])
  
    retdict[key] = scores[0]
    
  return retdict
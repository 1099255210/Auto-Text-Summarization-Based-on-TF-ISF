import readfile
import datapre
import similarity
import generatesummary
import saveresult
import judge
import json
import drawchart
import caltfisf
import s2v

def runSummary():

  data = readfile.get_data('./大作业/docs/')
  
  
  for folder in data.folderlist:
    senset = datapre.prepare_new(folder)
    
    
    # tfisf way
    # tfisfarr = caltfisf.getTFISF_new(senset)
    # similarvalue = similarity.getSimilarityArr_new(tfisfarr)
    # summary = generatesummary.generateSum_new(similarvalue, senset, tfisfarr, folder.foldername)
    # saveresult.saveSummary_new(summary, folder.foldername)
    
    # sentence2vec way
    s2v.traininit()
    vec = s2v.train(senset)
    similarvalue = similarity.getSimilarityArr_new(vec)
    summary = generatesummary.generateSum_new(similarvalue, senset, vec, folder.foldername)
    saveresult.saveSummary_new(summary, folder.foldername)


def runRouge():

  myresult = readfile.get_resultfile('./大作业/sum/')
  partresult = readfile.get_partresult(myresult)
  
  # my result
  compareres = judge.compare(myresult, partresult)
  with open('./大作业/result.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(compareres))
    
  # baseline
  with open('./大作业/baseline/bs.json', 'r', encoding='utf-8') as fp:
    baseline = json.loads(fp.read())
  compareres = judge.compareBaseline(baseline, partresult)
  with open('./大作业/result_baseline.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(compareres))
    
  drawchart.drawChart('rouge-1')
  drawchart.drawChart('rouge-2')
  drawchart.drawChart('rouge-l')
  
  
def saveBaseline():
  data = readfile.get_data('./大作业/docs/')
  baseline = datapre.prepareBaseline(data)
  with open('./大作业/baseline/bs.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(baseline))
  
  
'''
Main progress
'''

runSummary()
  
# saveBaseline()

runRouge()

# savechart()


'''
Some tests
'''

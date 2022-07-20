import datadef
import os
from typing import List

def saveSummary_new(summary:str, topicname:str):
  with open('./大作业/sum/' + topicname + '.txt', 'w', encoding='utf-8') as f:
    f.write(summary)
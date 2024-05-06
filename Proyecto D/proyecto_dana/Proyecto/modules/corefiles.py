import json
import os 

MY_DATABASE = "Datas_usuarios/"

def NewFile(*param):
     with open(MY_DATABASE,"w") as wf:
          json.dump(param[0],wf,indent=4)

def updateFile(*param):
     with open(MY_DATABASE,'w') as fw:
          json.dump(param[0],fw,indent=4)


def AddData(*param):
     data =list(param)
     with open(MY_DATABASE,"r+") as omu:
          file_data=json.load(omu)
          if (len(param)>1):
               file_data[data[0]].update({data[1]:data[2]})
          else:
               file_data.update({param[0]})
          omu.seek(0)
          json.dump(file_data,omu,indent=4)
def ReadFile():
     with open(MY_DATABASE,"r") as uf:
          return json.load(uf)
def SaveDate(*param):
     data=list(param)
     if(os.path.isfile(MY_DATABASE)):
          if(len(param)):
               data[0].update(ReadFile)
     else: 
               if(len(param)):
                    NewFile(data[0])

def checkFile(*param):
     data=list(param)
     if(os.path.isfile(MY_DATABASE)):
          if(len(param)):
               data[0].update(ReadFile())
          else:
               if(len(param)):
                    NewFile(data[0])

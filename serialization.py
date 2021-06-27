import pickle
import os
projectFolder = os.getcwd()


def saveData(hashandWords):
 
  with open(projectFolder + '\hash.bin', 'bw') as f:
    pickle.dump(hashandWords, f)


def readData():
  
  with open(projectFolder + '\hash.bin', 'br') as f:
    hashandWords = pickle.load(f)
    return hashandWords

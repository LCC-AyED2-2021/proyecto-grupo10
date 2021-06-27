import pickle
import os
projectFolder = os.getcwd()


def hacer_escritura(hashandWords):
 
  with open(projectFolder + '\hash.bin', 'bw') as f:
    pickle.dump(hashandWords, f)


def hacer_lectura():
  
  with open(projectFolder + '\hash.bin', 'br') as f:
    hashandWords = pickle.load(f)
    return hashandWords

import pickle

def hacer_escritura(hashandWords):

  with open('C:\Lucas\proyecto-grupo10\SavedHash\hash.bin', 'bw') as f:
    pickle.dump(hashandWords, f)


def hacer_lectura():
  
  with open('C:\Lucas\proyecto-grupo10\SavedHash\hash.bin', 'br') as f:
    hashandWords = pickle.load(f)
    return hashandWords

from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
from objets import *
from serialization import *
from create import *
from search import *
import os
import sys


print("Bienvenido a la Personal Library de TobyLucas")



if(sys.argv[1] == "-create"):
    #leemo el parametro 
    pathConsoleParamater = sys.argv[2]
    completePath = os.chdir(pathConsoleParamater)
    HashAndTotalWords = insertWordsHash(completePath)
    firstHash = HashAndTotalWords[0]
    totalWords = HashAndTotalWords[1]
    SecondHash = invertStructure(firstHash,totalWords)
    ResultToSave = HashAndWords(SecondHash,totalWords)
    saveData(ResultToSave)


elif(sys.argv[1] == "-search"):
    searchQuery = sys.argv[2]
    resultFromLecture = readData()
    sortedResults = searchLibrary(resultFromLecture.hash, searchQuery,resultFromLecture.words)
    print("LISTA ORDENADA:")
    if sortedResults != None:
        imprimirlista(sortedResults)
    
else:
   print("Ingrese un comando valido :)")









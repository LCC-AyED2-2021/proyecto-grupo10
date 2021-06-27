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
import random

print("Bienvenido a la Personal Library de TobyLucas")



if(sys.argv[1] == "-create"):
    print("Iniciando Create")
    pathParamater = sys.argv[2]
    path = os.chdir(pathParamater)
    result = insertWordsHash(path)
    firstD = result[0]
    totalWords = result[1]
    inverted = invertStructure(firstD,totalWords)
    result_to_save = HashAndWords(inverted,10)
    hacer_escritura(result_to_save)


elif(sys.argv[1] == "-search"):
    print("Iniciando Search")
    searchQuery = sys.argv[2]
    resultFromLecture = hacer_lectura()
    newList = searchNEW(resultFromLecture.hash, searchQuery,resultFromLecture.words)
    print("SEARCH")
    print("LISTA ORDENADA:")
    if newList != None:
        imprimirlista(newList)
    
else:
   print("Ingrese un comando valido :)")









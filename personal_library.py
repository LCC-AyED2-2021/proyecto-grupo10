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
    #leemos el parametro <local_path> por consola
    pathConsoleParamater = sys.argv[2]
    #creamos el path total
    completePath = os.chdir(pathConsoleParamater)
    #Insertamos en el primer hash
    HashAndTotalWords = insertWordsHash(completePath)
    firstHash = HashAndTotalWords[0]
    totalWords = HashAndTotalWords[1]
    #Insertamos en el segundo hash
    SecondHash = invertStructure(firstHash,totalWords)
    #Guardamos el segundo hash + las palabras totales de todos los documentos
    ResultToSave = HashAndWords(SecondHash,totalWords)
    saveData(ResultToSave)


elif(sys.argv[1] == "-search"):
    searchQuery = sys.argv[2]
    #leemos el parametro <key_word> por consola
    resultFromLecture = readData()
    #leemos del disco el hash y las palabras totales guardadas
    sortedResults = searchLibrary(resultFromLecture.hash, searchQuery,resultFromLecture.words)
    #Hacemos search de los resultados y lo guardamos en una lista para imprimirla
    if sortedResults != None:
    #mostramos los resultados
        imprimirlista(sortedResults)
    
else:
   print("Ingrese un comando valido :)")









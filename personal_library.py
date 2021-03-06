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

if(strcmp(String(sys.argv[1]) ,String("-create"))):
    print("Welcome to TobyLucas's Personal Library!")
    #leemos el parametro <local_path> por consola
    pathConsoleParamater = sys.argv[2]
    #creamos el path total
    completePath = os.chdir(pathConsoleParamater)
    #Insertamos en el primer hash
    print("Creating first structure...")
    HashAndTotalWords = insertWordsHash(completePath)
    firstHash = HashAndTotalWords[0]
    totalWords = HashAndTotalWords[1]
    #Insertamos en el segundo hash
    print("Creating second Hash...")
    SecondHash = invertStructure(firstHash,totalWords)
    #Guardamos el segundo hash + las palabras totales de todos los documentos
    ResultToSave = HashAndWords(SecondHash,totalWords)
    saveData(ResultToSave)
    print("Library created successfully!")
elif(strcmp(String(sys.argv[1]) ,String("-search"))):
    searchQuery = sys.argv[2]
    #leemos el parametro <key_word> por consola
    resultFromLecture = readData()
    #leemos del disco el hash y las palabras totales guardadas
    print("Initializing search...")
    sortedResults = searchLibrary(resultFromLecture.hash, searchQuery,resultFromLecture.words)
    #Hacemos search de los resultados y lo guardamos en una lista para imprimirla
    if sortedResults != None:
    #mostramos los resultados
        print("This are the results:")
        print("------------------------------------------------------")
        imprimirlista(sortedResults)
        print("------------------------------------------------------")
    else:
        print("No document found.")
    
else:
   print("Ingrese un comando valido :)")









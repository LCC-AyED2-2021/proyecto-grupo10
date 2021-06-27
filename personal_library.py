from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
from objets import *
from serialization import *
import os
import sys
import random

print("Bienvenido a la Personal Library de TobyLucas")
#path = os.chdir('C:\Lucas\Prueba Algoritmos')
path = os.chdir(r'C:\Users\Tobias\Documents\archivos de prueba')

result = insertWordsHash(path)
firstD = result[0]
totalWords = result[1]
print("TOTAL WORDS ", totalWords)
printD2(firstD)

#if(sys.argv[1] == "-create"):
 #   print("Iniciando Create")
    #pathParamater = sys.argv[2]
    #path = os.chdir(pathParamater)
    #ejecutar create
    #inverted = invertStructure(firstD)
    #result_to_save = HashAndWords(firstD,10)
    #hacer_escritura(result_to_save)
    #persisto el hash en disco

#elif(sys.argv[1] == "-search"):
 #   print("Iniciando Search")
    #searchQuery = sys.argv[2]
    #result_from_lecture = hacer_lectura()
    #print(result_from_lecture.words)
    #ejecutar search
#else:
 #   print("Ingrese un comando valido :)")


'''''
##FUNCION HASH
def hash(key):
  slot = 0
  for i in range(0, len(key)):
    slot = slot + (ord(key[i]) * 256^i)

  return slot % totalWords
'''

#PERFECT HASH
G = Array(totalWords + 1, 0)
for i in range(0, totalWords + 1):
    G[i] = random.randrange(0, totalWords)

S1 = Array(totalWords + 2, 0)
S2 = Array(totalWords + 2, 0)
for i in range(0, totalWords + 2):
    S1[i] = random.randrange(0, totalWords)
    S2[i] = random.randrange(0, totalWords)

def hash_f(key, T):
    return sum(T[i % totalWords] * ord(c) for i, c in enumerate(str(key))) % len(G)

def hash(key):
    return (G[hash_f(key, S1)] + G[hash_f(key, S2)]) % len(G)


#Función que desde el primer hash, crea un segundo hash con cada palabra apuntando a un archivo con la cantidad de veces que se encuentra dicha palabra en el archivo
def invertStructure(S):
    inverted = Array(totalWords, dictionary())

    for i in range(0, len(S)):

        currentNode = S[i].head.nextNode #en la cabeza de la lista tenemos el nombre del archivo

        while currentNode != None:
            slot = hash(currentNode.value)
            print("SLOT DE ", currentNode.value, " ES ", slot)

            if inverted[slot] == None: #si el slot está vacío, agregamos la palabra y el nombre del archivo (este ultimo en la cabecera)
                L = dictionary()
                addToDictionary(L, currentNode.value, slot)
                addToDictionary(L, S[i].head.value, slot)
                inverted[slot] = L
                
            elif inverted[slot].head.value == S[i].head.value:
                inverted[slot].head.repetitions = inverted[slot].head.repetitions + 1

            else:
                addToDictionary(inverted[slot], S[i].head.value, slot)

            
            currentNode = currentNode.nextNode



    print("succesful!")
    return inverted

def searchNEW(inverted, word):

    slot = hash(word)
    print("SLOT ", slot)

    if inverted[slot] != None:
        List = inverted[slot]
        print("LISTA SIN ORDENAR:")
        delete(List, word)
        imprimirlista(List)
        newList = ordenarLista(List)

        return newList

    print("No se encontró la palabra.")
    return None

inverted = invertStructure(firstD)
print("NEXT")
printD(inverted)
newList = searchNEW(inverted, "Hola")
print("SEARCH")
print("LISTA ORDENADA:")
imprimirlista(newList)
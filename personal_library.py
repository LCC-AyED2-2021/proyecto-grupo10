from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
import os

print("Bienvenido a la Personal Library de TobyLucas")
#path = os.chdir('C:\Lucas\Prueba Algoritmos')
path = os.chdir(r'C:\Users\Tobias\Documents\Facultad\Segundo año\AED 2\documentos algo2')

result = insertWordsHash(path)
firstD = result[0]

totalWords = result[1]
print("tw", totalWords)

##FUNCION HASH
def hash(key):
  slot = 0
  for i in range(0, len(key)):
    slot = slot + ord(key[i]) - ord("a")
  return slot % totalWords

#Función que desde el primer hash, crea un segundo hash con cada palabra apuntando a un archivo con la cantidad de veces que se encuentra dicha palabra en el archivo
def invertStructure(S):
    slotsQ = 0

    inverted = Array(totalWords, dictionary())

    for i in range(0, len(S)):

        currentNode = S[i].head.nextNode #en la cabeza de la lista tenemos el nombre del archivo

        while currentNode != None:
            slot = hash(currentNode.value)

            if inverted[slot] == None: #si el slot está vacío, agregamos la palabra y el nombre del archivo (este ultimo en la cabecera)
                L = dictionary()
                addToDictionary(L, currentNode.value, slot)
                addToDictionary(L, S[i].head.value, slot)
                inverted[slot] = L
            else: #si no está vacío, le sumamos a la cabecera (donde tenemos el nombre del archivo), 1 (esto significa que se repite la palabra en ese archivo)
                inverted[slot].head.repetitions = inverted[slot].head.repetitions + 1
            
            currentNode = currentNode.nextNode

    print("succesful!")
    return inverted

def searchNEW(inverted, word):

    slot = hash(word)
    print("SLOT ", slot)

    if inverted[slot] != None:
        List = inverted[slot]
        imprimirlista(List)
        delete(List, word)

        newList = MergeSort(List)

        return newList

    return None

inverted = invertStructure(firstD)
newList = searchNEW(inverted, "for")
print("NEXT")
imprimirlista(newList)
#printD(inverted)
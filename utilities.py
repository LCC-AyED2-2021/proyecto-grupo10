from mydicctionary import dictionary, dictionaryNode
from algo1 import *
from mylinkedlist import *
from math import *
import os
#from typing import List


def check_file_count(path):
    files = os.listdir(path)
    for names in files:
        print(names)
    file_count = len(files)
    print("La cantidad de archivos en la carpeta es " + str(file_count))

    return file_count

def ordenarLista(lista):
    if lista.head == None:
        return None
    else:
        #recorremos todos los nodos de la lista
        count = 0
        while count <= length(lista):
            #comparamos
            currentNode = lista.head
            while currentNode != None:

                if currentNode.nextNode != None:
                    #si se cumple la condicion cambiamos los valores
                    if currentNode.repetitions > currentNode.nextNode.repetitions:
                        nodoAuxiliar = igualarNodos(currentNode)
                        currentNode.value = currentNode.nextNode.value
                        currentNode.repetitions = currentNode.nextNode.repetitions
                        currentNode.nextNode.value = nodoAuxiliar.value
                        currentNode.nextNode.repetitions = nodoAuxiliar.repetitions

                currentNode = currentNode.nextNode
            count = count + 1

        #invertimos la lista

        newlist = dictionary()
        currentNode = lista.head

        while currentNode != None:
            newNode = dictionaryNode()
            newNode.value = currentNode.value
            newNode.repetitions = currentNode.repetitions
            newNode.nextNode = newlist.head
            newlist.head = newNode

            currentNode = currentNode.nextNode

        ## retornamos la lista con el orden realizada
        return newlist
    
    return None

def igualarNodos(Nodo):
    NewNode = Node()
    NewNode.value = Nodo.value
    NewNode.repetitions = Nodo.repetitions
    NewNode.nextNode = Nodo.nextNode
    return NewNode


    


            



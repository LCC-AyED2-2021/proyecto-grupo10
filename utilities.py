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

def insertOnStructure(D, slot, word):
    if word != '':
        if D[slot] == None:
            L = LinkedList()
            add(L, word)
            D[slot] = L
        else:
            add(D[slot], word)


def insertWordsHash(path):
    files = os.listdir(path)
    
    global totalWords #variable que guarda el total de palabras entre todos los textos, aunque se repitan
    totalWords = 0
    
    firstDictionary = Array(len(files), LinkedList())
    j = 0

    for file in files:
        f = open(file, encoding="utf8")
        lines = f.readlines()

        for line in lines:
            word = ''
            lentghL = len(line)
            for i in range(0,lentghL):
                
                if line[i] != '.' and line[i] != ',' and line[i] != ' ' and line[i] != '(' and line[i] != ')' and line[i] != '"' and line[i] != '\n':
                    word = word + line[i]

                    if i == lentghL - 1:
                        insertOnStructure(firstDictionary, j, word)
                        totalWords = totalWords + 1

                else:
                    
                    if i < lentghL - 2 and ((line[i] == '.' and line[i+1] != ' ') or (line[i] == ',' and line[i+1] != ' ')):
                        word = word + line[i]

                    insertOnStructure(firstDictionary, j, word)

                    totalWords = totalWords + 1
                    word = ''
                
        insertOnStructure(firstDictionary, j, file)
        j = j + 1
    
    print("succesful!")
    return firstDictionary, totalWords

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


    


            



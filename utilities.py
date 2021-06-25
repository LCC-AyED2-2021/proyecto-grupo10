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
                
                if line[i] != '.' and line[i] != ',' and line[i] != ' ' and line[i] != '(' and line[i] != ')' and line[i] != '"':
                    word = word + line[i]

                    if i == lentghL - 2:
                        insertOnStructure(firstDictionary, j, word)

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

def MergeSort(lista):
    if length(lista) <= 1:
        return lista
    else:
        #dividimos la lista principal en 2 listas 
        parteIzquierda = LinkedList()
        parteDerecha = LinkedList()
        centro = trunc(length(lista) / 2)
        currentNode = lista.head

        for n in range(0, length(lista)):
            if n < centro:
                enqueue(parteIzquierda, currentNode.repetitions)
            else:
                enqueue(parteDerecha, currentNode.repetitions)
            currentNode = currentNode.nextNode

        parteIzquierda = MergeSort(parteIzquierda)
        parteDerecha = MergeSort(parteDerecha)
        ##llamamos la funcion hasta que las listas esten ordenadas
        #Si las listas se estan ordenadas las juntaos y se devuelven
        if access(parteIzquierda, length(parteIzquierda) - 1) <= access(parteDerecha, 0):
            currentNode = parteDerecha.head
            while currentNode != None:
                enqueue(parteIzquierda, currentNode.repetitions)
                currentNode = currentNode.nextNode
            return parteIzquierda

        listaOrdenada = MergeSortR(parteIzquierda, parteDerecha)
        ## retornamos la lista con la busqueda realizada
        return listaOrdenada

def MergeSortR(lista1, lista2):

    listaaOrdenar = LinkedList()

    #ordenamos los valores
    ##correspondientes a cada lista
    ##luego juantamos las listas en una
    while length(lista1) > 0 and length(lista2) > 0:
        #
        if access(lista1, 0) <= access(lista2, 0):
            enqueue(listaaOrdenar, access(lista1, 0))
            delete(lista1, access(lista1, 0))
        else:
            enqueue(listaaOrdenar, access(lista2, 0))
            delete(lista2, access(lista2, 0))
    if length(lista1) > 0:
        currentNode = lista1.head
        while currentNode != None:
            enqueue(listaaOrdenar, currentNode.repetitions)
            currentNode = currentNode.nextNode
    if length(lista2) > 0:
        currentNode = lista2.head
        while currentNode != None:
            enqueue(listaaOrdenar, currentNode.repetitions)
            currentNode = currentNode.nextNode
    return listaaOrdenar


    


            



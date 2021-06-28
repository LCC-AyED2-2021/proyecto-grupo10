from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
from objets import *
from serialization import *
import os
import sys



##FUNCION HASH
def hash(s, totalWords):
    val = 0
    for i in range(len(s)):
        j = abs(i - len(s))
        val += (ord(s[i])*(255^j))

    return val  % totalWords

#Inserción de palabras de los textos a una primera estructura.
#Cada archivo se encuentra en la cabecera de un slot, apuntando a una lista que contiene todas las palabras del archivo
def insertWordsHash(path):
    files = os.listdir(path)
    
    totalWords = 0 #variable que guardará la cantidad total de palabras
    
    firstDictionary = Array(len(files), LinkedList()) #creamos la primer estructura con la cantidad de slots como archivos existan.
    j = 0 #variable que representa el slot de la estructura.

    for file in files: #recorremos los archivos
        f = open(file, encoding="utf8")
        lines = f.readlines()

        for line in lines: #recorremos cada línea
            word = String('') #creamos una palabra vacía a la cual concatenaremos cada caracter que sea una letra o palabra.
            lentghL = len(line) #guardamos la longitud de la línea

            for i in range(0,lentghL): #recorremos cada caracter
                
                #En el siguiente IF, despreciaremos aquellos caracteres que sean iguales a un punto, coma, espacio, parentesis, comillas y ENTER.
                if line[i] != '.' and line[i] != ',' and line[i] != ' ' and line[i] != '(' and line[i] != ')' and line[i] != '"' and line[i] != '\n':
                    word = concat(word, String(line[i])) #Si el caracter es distinto a los ya mencionados, significa que es una letra, por lo que la concatenamos

                    if i == lentghL - 1: #Condición para poder guardar la última palabra de la línea
                        insertOnStructure(firstDictionary, j, word)
                        totalWords = totalWords + 1

                else:
                    
                    #La siguiente condición se encarga de ver si el caracter luego de un punto o una coma es un espacio, 
                    #si no lo es, podríamos estar tratando con un número con coma o un mail, por lo que concatenaremos el caracter al string
                    if i < lentghL - 2 and ((line[i] == '.' and line[i+1] != ' ') or (line[i] == ',' and line[i+1] != ' ')):
                        word = concat(word, String(line[i]))

                    insertOnStructure(firstDictionary, j, word)

                    totalWords = totalWords + 1
                    word = String('')
                
        insertOnStructure(firstDictionary, j, String(file)) #Por último, insertamos el nombre del archivo en la cabecera del slot.
        j = j + 1
        f.close()

    return firstDictionary, totalWords #Devolveremos la estructura y el total de palabras.

#Función que desde el primer hash, crea un segundo hash con cada palabra apuntando a un archivo con la cantidad de veces que se encuentra dicha palabra en el archivo
def invertStructure(S,totalWords):
    inverted = Array(totalWords, dictionary()) #Creamos la estructura, con la cantidad de slots como palabras hayan.

    for i in range(0, len(S)): #recorremos cada slot

        currentNode = S[i].head.nextNode #en la cabeza de la lista tenemos el nombre del archivo

        while currentNode != None: #recorremos cada lista
            slot = hash(currentNode.value,totalWords)
            

            if inverted[slot] == None: #si el slot está vacío, agregamos la palabra y el nombre del archivo (este ultimo en la cabecera)
                L = dictionary()
                addToDictionary(L, currentNode.value, slot)
                addToDictionary(L, S[i].head.value, slot)
                inverted[slot] = L
                
            elif inverted[slot].head.value == S[i].head.value: #si ambas cabeceras son iguales, significa que la palabra con la que estamos tratando ya está en el archivo
                inverted[slot].head.repetitions = inverted[slot].head.repetitions + 1 #sumamos 1 a la cantidad de veces que se repite la palabra

            else: #si no se cumple ninguna de las anteriores, significa que estamos tratando con un nuevo archivo
                addToDictionary(inverted[slot], S[i].head.value, slot)

            
            currentNode = currentNode.nextNode

    return inverted #retornamos el nuevo hash

def insertOnStructure(D, slot, word): #Función de inserción en la estructura.
    if strcmp(word, String("")):
        if D[slot] == None:
            L = LinkedList()
            add(L, word)
            D[slot] = L
        else:
            add(D[slot], word)



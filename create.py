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
        f.close()
    return firstDictionary, totalWords

#Función que desde el primer hash, crea un segundo hash con cada palabra apuntando a un archivo con la cantidad de veces que se encuentra dicha palabra en el archivo
def invertStructure(S,totalWords):
    inverted = Array(totalWords, dictionary())

    for i in range(0, len(S)):

        currentNode = S[i].head.nextNode #en la cabeza de la lista tenemos el nombre del archivo

        while currentNode != None:
            slot = hash(currentNode.value,totalWords)
            

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



    
    return inverted

def insertOnStructure(D, slot, word):
    if word != '':
        if D[slot] == None:
            L = LinkedList()
            add(L, word)
            D[slot] = L
        else:
            add(D[slot], word)



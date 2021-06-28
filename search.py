from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
from objets import *
from create import *
from serialization import *



#Función que desde la librería, retorna una lista de archivos que contienen esa palabra, ordenados por relevancia
def searchLibrary(inverted, word ,totalWords):

    slot = hash(word,totalWords) #Conseguimos el slot de la palabra correspondiente
    strWord = String(word) #Pasamos la palabra a string de algo1

    if inverted[slot] != None: #Condición que verifica que el slot no esté vacío
        List = inverted[slot]
        
        #Primero, eliminaremos la palabra de la lista para que sea más fácil ordenarla,
        #en caso que no se encuentre la palabra, significa que hay colisión pero que no es la palabra que queremos buscar.
        if delete(List, strWord) != None:
            newList = ordenarLista(List)
            return newList

    return None
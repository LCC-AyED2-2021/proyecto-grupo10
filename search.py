from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
from objets import *
from create import *
from serialization import *




def searchLibrary(inverted, word ,totalWords):

    slot = hash(word,totalWords)

    if inverted[slot] != None:
        List = inverted[slot]
        print("LISTA SIN ORDENAR:")
        delete(List, word)
        imprimirlista(List)
        newList = ordenarLista(List)

        return newList

    print("No se encontró la palabra.")
    return None
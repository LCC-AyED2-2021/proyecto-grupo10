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
    strWord = String(word)

    if inverted[slot] != None:
        List = inverted[slot]
        if delete(List, strWord) != None:
            newList = ordenarLista(List)
            return newList

    return None
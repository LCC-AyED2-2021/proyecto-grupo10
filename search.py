from mydicctionary import *
from algo1 import *
from mydicctionary import *
from mylinkedlist import *
from utilities import *
from objets import *
from serialization import *
import os
import sys



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
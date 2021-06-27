##TP4 LISTAS
##Lucas Bloise

from algo1 import *


class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


def add(L, element):
    currentNode = Node()
    ##generamos una posicion en memoria con un nuevo nodo
    currentNode.value = element
    ##establecemos el valor del nodo inicial
    currentNode.nextNode = L.head
    ##establecemos que el proximo node va a ser lo primero que este en la lista que pasamos
    L.head = currentNode
    ##establecemos el nodo inicial de esta lista va ser el que generamos al principio
    #notación  O(1)
    return currentNode
    ##el return no esta definido, pero creo que lo mas optimo es retornar el nodo actual


def search(L, element):
    currentNode = L.head
    ##establecemos el currentNode como el primer nodo de la lista
    position = None
    ##establecemos una posicion nula al empezar, es lo que retornamos si se encuentra un elemento o no
    contador = 0
    while currentNode != None:
        if currentNode.value == element:
            position = contador
            break
        contador = contador + 1

        currentNode = currentNode.nextNode

    return position


def length(L):
    currentNode = L.head
    ##establecemos el nodo actual como el comienzo de la lista
    elementoCount = 0
    ##recorremos la lista mientra no este un none va a contar los elementos
    while currentNode != None:
        elementoCount = elementoCount + 1
        currentNode = currentNode.nextNode
        #notación O(n)
    return elementoCount


def insert(L, element, position):
    currentNode = L.head
    ##establecemos el nodo actual como el comienzo de la lista
    contador = 0
    if position == 0:
        add(L, element)
    nodo = Node()
    nodo.value = element

    if length(L) < position or position < 0:
        position = None

    while currentNode != None:
        if position - 1 == contador:
            nodo.nextNode = currentNode.nextNode
            currentNode.nextNode = nodo
            currentNode.nextNode.nextNode = nodo.nextNode
        contador = contador + 1
        currentNode = currentNode.nextNode

#notación O(n)
    return position


##tuve que cambiar mi delete porque no funcionaba anteriormente como lo tenia en mi linked list :(
def delete(L, element):
    Posicion = search(L, element)
    if Posicion != None:
        currentnode = L.head
        while currentnode != None:
            if L.head.value == element:
                L.head = L.head.nextNode
                break
            elif currentnode.nextNode.value == element:
                currentnode.nextNode = currentnode.nextNode.nextNode
                break
            currentnode = currentnode.nextNode
    return Posicion


def access(L, position):
    valor = None
    currentNode = L.head
    ##establecemos el nodo actual como el comienzo de la lista
    contador = 0
    while currentNode != None:
        if contador == position:
            ##accedemos al valor solicitado en la posicion solicitada
            valor = currentNode.value
            break
        contador = contador + 1
        currentNode = currentNode.nextNode
    #notación O(n)
    return valor


def update(L, element, position):
    currentNode = L.head
    posicion = None
    contador = 0
    if access(L, position) != None:
        ##usamos access para cuequear que el valor sea distinto de none
        while currentNode != None:
            if contador == position:
                currentNode.value = element
                posicion = position
                break
            contador = contador + 1
            currentNode = currentNode.nextNode


#notación O(n)
    return posicion


def imprimirlista(l):
    currentNode = l.head
    while currentNode != None:
        print(currentNode.value)
        currentNode = currentNode.nextNode


def enqueue(Q,element):
	insert(Q,element,length(Q))


def dequeue(Q):
    if length(Q) == None:
        element = None
    else:
        element = (access(Q, 0))
        delete(Q, access(Q, 0))
    return element


def push(S, element):
    add(S, element)
    return


def pop(S):

    element = None
    if S.head != None:
        element = access(S, 0)
        delete(S, access(S, 0))

    return element


def igualarNodos(Nodo):
    NewNode = Node()
    NewNode.value = Nodo.value
    NewNode.nextNode = Nodo.nextNode
    return NewNode

##creo una funcion que chequea los elementos repetidos de una lista
def revisarRepetidos(lista, elemento):
  if lista.head!=None:
    currentNode=lista.head.nextNode
    value=lista.head.value
    contador=1
    while currentNode!=None:
      if currentNode.value==value:
        contador=contador+1
      currentNode=currentNode.nextNode

    if contador==length(lista):
      for i in range(0, contador):
        add(elemento, value)
      lista.head=None
      return True
    else:
      return False
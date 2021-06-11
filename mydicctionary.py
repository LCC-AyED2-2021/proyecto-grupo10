##TP5 Ejercitación  Hash Tables
## Lucas Bloise
#A partir de estructuras definidas como :
#
#class dictionary:
#  head = None
#
#class dictionaryNode:
#  value = None
#  key = None
#  nextNode = None

from algo1 import *
from mylinkedlist import*
from array import *

class dictionary:
  head = None

class dictionaryNode:
  value = None
  key = None
  nextNode = None

slotsSize = 9




##FUNCION HASH
def hash(key):
 return key%slotsSize



#insert(D,key, value)
#Descripción: Inserta un key en una posición determinada por la función de hash similar a (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de existir un hash(Key) duplicado, el key se anexa a la lista.
#Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
#Salida: Devuelve D

def insertH(D, key, value):
  slot = hash(key)
  if D[slot] == None:
    L = dictionary()
    addToDictionary(L, value, key)
    D[slot] = L
  else:
    addToDictionary(D[slot], value, key)
  
  return D

def addToDictionary(D, element, key):
  ##agrega el el elemento al diccionario
  newNode = dictionaryNode()
  newNode.value = element
  newNode.key = key
  newNode.nextNode = D.head
  D.head = newNode

#search(D,key)
#	Descripción: Busca un key en el diccionario
#Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
#Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
def searchH(D, key):
  slotHash = hash(key)
  if D[slotHash] != None:
    currentNode = D[slotHash].head

    while currentNode != None:
      if currentNode.key == key:
        return key
      currentNode = currentNode.nextNode
  return None


#delete(D,key)
#Descripción: Elimina un key en la posición determinada por una función de hash similar (1) del diccionario (dictionary) 
#Poscondición: Se debe marcar como nulo  el key  a eliminar.  
#Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
def deleteHash(D, key):
  slotHash = hash(key)
  currentNode = D[slotHash].head
  while currentNode != None:
    if currentNode.key == key:
      currentNode.key = None
      return currentNode.value
    currentNode = currentNode.nextNode
  
  return None

#Ejercicio 4
#Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
def checkPermutation(s, p):
  lengthS = len(s)
  lengthP = len(p)

  if lengthS == lengthP:
    ordS = 0
    ordP = 0
    for i in range(0, lengthS):
      ordS = ordS + ord(s[i])
      ordP = ordP + ord(p[i])
    
    if ordP == ordS:
      return True
  
  return False

#Ejercicio 5
#Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución propuesta.

def checkUnique(L):
    slotSize = 29
    D = Array(slotSize,dictionary())
    dimensionL = len(L)

    for i in range(0,dimensionL):
        if(insertUnique(D,L[i],None) == False):
           return False

    return True

    
def insertUnique(D, key, value):
    slotHash = hash(key)
    #obtenemos el slot donde se almacena 
    if(D[slotHash] == None):
        L = dictionary()
        D[slotHash] = L
        addToDictionary(L,value,key)
    else:
        if(searchH(D, key) != None):
            return False
        else:
            addToDictionary(D[slotHash],value,key)

    return True



#Ejercicio 6
#Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Diseñar e implementar una función de hash apropiada para los códigos postales argentinos.
def hashPostalCode(postalCode):

  if len(postalCode) == 8:
    total = 0

    for i in range(0, 8):
      total = total + ord(postalCode[i])
    
    return hash(total - ord("A"))
  
  return None


#Ejercicio 7
#Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
def strcompress(s):
  length = len(s)
  D = Array(slotsSize,dictionary())
  n = 1
  stringToCompress = ""
  for i in range(0,length):

    if searchH(D,s[i]) != None:
      n = n + 1
    else: 
      insertH(D,s[i],s[i])
      if n == 1:
        stringToCompress = stringToCompress + s[i]  
      else:
        deleteHash(D,s[i-1]) 
        stringToCompress = stringToCompress + str(n) + s[i] 
        n = 1

  if i == length-1:
    if n != 1:          
      stringToCompress = stringToCompress+str(n)     
        
     
  return stringToCompress

#Ejercicio 8
#Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta).  Justificar el coste en tiempo de la solución propuesta.
def checkSubString(s, p):

  lengthS = len(s)
  lengthP = len(p)

  n = 0

  for i in range(0, lengthS):
    if s[i] == p[n]:
      n = n + 1
      if n == 1:
        firsString = i
      if n == lengthP:
        return firsString
    else:
      n = 0
      firsString = None

  return None

#Ejercicio 9
#Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
def checkSubSet(s, p):

  D = Array(9, dictionary())
  colisions = 0

  lengthS = len(s)
  lengthP = len(p)

  for i in range(0, lengthS):
    insertH(D, s[i], s[i])
  
  for i in range(0, lengthP):
    if searchH(D, p[i]) != None:
      colisions = colisions + 1

  if colisions == lengthP:
    return True
  else:
    return False


#Funciones Auxiliares para el Tp:

#Imprime un diccionario con colisiones encadenadas
#El formato de los nodos es [k: key ;v: value]
#Creditos a Gabriel Gonzalez Sanchez que la paso por slack y me sirvio un monton :)
def printD(D):
    n = len(D)
    for i in range(0,n):
        currentNode = D[i]
        if currentNode!=None:
            currentNode = D[i].head
            print("Slot",i,': ',end='')
            while currentNode!=None:
                if currentNode.nextNode!=None:
                        print("[k:",currentNode.key,";v:",currentNode.value,"] ➝ ",end="")
                else:
                    print("[k:",currentNode.key,";v:",currentNode.value,"] ➝ ",currentNode.nextNode,"\n") 
                currentNode = currentNode.nextNode
        else:
            print("Slot",i,": ",currentNode,"\n")


 
  
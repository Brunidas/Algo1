# Bruno Fuentes
# 12401
# bruno.e.fuentes97@gmail.com

from algo1 import*
from queue import*
from linkedlist import*



def isPermutation(L,S): 
    """
    Dadas dos listas (LinkedList) L y S, conteniendo numeros del 0 al 255 , escribir una funcion isPermutation(L,S) que determine si S es una permutación (mismos elementos con diferente orden) de L. Implementar una versión cuya complejidad sea O(n).
    """
    
    
    vector = Array(256,0)   # se guardan la cantidad de elemmentos repetidos


    for i in range( len(vector) ):
        vector[i] = 0

    # print(vector)

    # recorro la lista L
    currentNode = L.head
    for i in range( length(L) ):
        vector[ access(L,i) ] += 1 
        currentNode = currentNode.nextNode 


    # recorro la lista S
    currentNode = S.head
    for i in range( length(S) ):
        vector[ access(S,i) ] += 1 
        currentNode = currentNode.nextNode 

    # print(vector)
    # recorro el vector y si tiene algun valor distinto de 0 y 2
    for i in range(len(vector) ):
        if vector[i] != 0 and vector[i] != 2:
            return False

    return True









L =  LinkedList()
add(L,4)
add(L,3)
add(L,2)
add(L,1)
printLinkedList(L)

S = LinkedList()
add(S,4)
add(S,3)
add(S,1)
add(S,2)
printLinkedList(S)


print(isPermutation(L,S) )
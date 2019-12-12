# Bruno Fuentes
# 12401
# heap_sort.py

from algo1 import*
from binary_heap import*

import linkedlist
from random import randint



def heapsort(L):
    BH = Bheap()
    listaInterna = linkedlist.LinkedList() 


    #copiar valores
    for i in range( linkedlist.length(L)-1 , -1 , -1 ):
        linkedlist.add(listaInterna, linkedlist.access(L,i) )
    
    heapify(BH,listaInterna)

    for i in range( length(BH) ):
        if length(BH) == 1:
            primero = linkedlist.access(BH.bheaplist,1) 
            linkedlist.add(listaInterna, primero)
        else:
            shiftDown(BH,1)   
            
            # intercambia el primero con el ultimo
            primero = linkedlist.access(BH.bheaplist,1) 
            ultimo = linkedlist.access(BH.bheaplist, length(BH))

            linkedlist.update(BH.bheaplist,primero, length(BH) )
            linkedlist.update(BH.bheaplist,ultimo, 1)

            # se coloco esta liena para que sea mas facil leer el codigo
            ultimo = primero    
            
            # se agrega el primero a listaInterna y se elimina el ultimo elemento
            # del Bheap
            linkedlist.add(listaInterna, ultimo)
            linkedlist.delete(BH.bheaplist,ultimo)


    # actualizar valores
    for i in range( linkedlist.length(L) ):
        linkedlist.update(L, linkedlist.access(listaInterna,i), i)

# URL : https://repl.it/@BrunoFuentes/Binary-Heaps-y-HeapSort
# Bruno Fuentes
# 12401


# binary_heap.py
from algo1 import*
import linkedlist
from random import randint

class Bheap:
    """ Estructura Bheap, lo unico que tiene una referencia a un lista.
    """
    bheaplist=linkedlist.LinkedList()
    def __str__(self):
            """ Permite hacer un print a una estructura Bheap
            """
            str_list=""
            current=self.bheaplist.head.nextNode
            while current!=None:
                str_list= str_list+str(current.value)+" "
                current=current.nextNode
            return(str_list)



def delMax(BH):
    """ 
    Recupera el mayor elemento del heap. Este siempre se encontrara al comienzo (posicion 1).
    Para manter la esctrucura del arbol binario se reemplaza el nodo raiz por el ultimo nodo.
    
    Luego mediante la funcion shiftDown se va recorriendo el arbol hasta encontrar la posicion 
    correcta de dicho nodo. De esta manara se garantiza la propiedad heap.
    """

    retval = linkedlist.access(BH.bheaplist,1 )
    ultimo = linkedlist.access(BH.bheaplist, length(BH) )

    linkedlist.delete(BH.bheaplist, ultimo)
    linkedlist.update(BH.bheaplist,ultimo,1)

    shiftDown(BH,1)

    return retval


def shiftUp(BH,i):
    """ Recorre el arbol desde los nodos hacia la raiz y va reemplazando el nodo i por su padre
        siempre y cuando i sea mayor. La operacion matematica i // 2 nos permite rapidamente encontrar al padre.
    """

    
    
    while i // 2 > 0:
        padre = linkedlist.access(BH.bheaplist, i//2)
        hijo = linkedlist.access(BH.bheaplist, i)

        if  padre < hijo:
            linkedlist.update(BH.bheaplist,padre,i)
            linkedlist.update(BH.bheaplist,hijo,i//2)


        i = i // 2

def shiftDown(BH,i,currentsize=None):
    """ Recorre el arbol desde la raiz y  hacia los nodos (arriba hacia abajo) va reemplazando el nodo i por sus hijos
        siempre y cuando alguno de sus hijos sea mayor. 
    """
    if currentsize==None:
        currentsize=linkedlist.length(BH.bheaplist)-1
    
    while (i * 2) <= currentsize:
        #indice del hijo mayor
        mc = maxChild(BH,i,currentsize) 
                                        
        padre = linkedlist.access(BH.bheaplist,i)
        hijoMayor = linkedlist.access(BH.bheaplist,mc)
        if hijoMayor > padre:
            linkedlist.update(BH.bheaplist,hijoMayor,i)
            linkedlist.update(BH.bheaplist,padre,mc)
    
        i = mc

def maxChild(BH,i,currentsize):
    """ Determina dado un nodo i, cual de sus hijos es el mayor y devuelve la posicion 
    """
    if i * 2 + 1 > currentsize:
        return i * 2
    else:
        if linkedlist.access(BH.bheaplist,i*2) > linkedlist.access(BH.bheaplist,i*2+1):
            return i * 2 
        else:
            return i * 2 + 1
    
def insert(BH,k):
    """ Inserta un elemento en el heap. Si la lista esta vacia, se crea un elemento 0. Este ultimo no se utiliza,
        pero facilita las operaciones matematicas para acceder a los padres e hijos. 
    """
    pos=linkedlist.length(BH.bheaplist)
    if pos==0:
        linkedlist.add(H.bheaplist,0)
        pos=pos+1
    linkedlist.insert(BH.bheaplist,k,pos)
    currentsize=linkedlist.length(BH.bheaplist)-1
    

    shiftUp(BH,currentsize)

def heapify(BH,L):
    """ Dada una lista crea un heap con complejidad temporal O(n)
    
    """
    i = linkedlist.length(L) // 2
    BH.bheaplist.head = L.head 
    linkedlist.add(BH.bheaplist,0)
    while (i > 0):
        shiftDown(BH,i)
        i = i - 1

def length(BH):
    return linkedlist.length(BH.bheaplist)-1


# ·······························································
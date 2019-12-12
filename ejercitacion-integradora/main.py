from algo1 import*
from binary_heap import*
from heap_sort import*
from queue import*
from z import*
from binarytree import*



import linkedlist
"""
Ejercicio 1
Dada una matriz de M x N en la cual, cada fila y columna  se encuentran ordenadas de manera  ascendente. Implementar un algoritmo para encontrar un elemento cuya complejidad sea al menos del orden de 0(M Log N).
"""
def valorEnMatriz(matriz, e):
    # representas indices de mayor tamaño
    M = len(matriz)-1
    N = len(matriz[0])-1 
    
    # comprueba si e esta en la matriz
    if e > matriz[0][0]:
        return None   # devuelve None si e no se 
    else:             # encunetra en la matriz
        if e < matriz[M][N]:
            return None
        else:
            indiceFila=0
            for i in range(0, M+1):
                if e >= matriz[i][N]:
                    indiceFila = i
                    break

            indiceCol=0
            for i in range(0,N+1):
                if e == matriz[indiceFila][i]:
                    indiceCol = i
                    break

            print("i: "+str(indiceFila))
            print("j: "+str(indiceCol))

# M=2
# N=2
# matriz = Array(M,Array(N,0))
# matriz[0][0]= 3
# matriz[0][1]= 2
# matriz[1][0]= 1
# matriz[1][1]= 0
# printMatrix(matriz)
# valorEnMatriz(matriz,3)



"""
(falta terminar)

Ejercicio 2
Implementar una versión recursiva  de la función subset(L), la cual dada una lista L de elementos no repetidos, devuelva una Lista con todos los posibles subconjuntos. Ejemplo: L = [1,2], -> {},{1},{2}.{1,2}.

"""
def subsetRecurive(L,tam):
    
    for i in range(0,linkedlist.length(L)-1):
        print("i:"+str(i))
        listaR = linkedlist.LinkedList()
        currentnode = L.head
        linkedlist.add(listaR,currentnode.value)
        if i==0:
            next = currentnode.nextNode
        
        linkedlist.add(listaR,next.value)
        linkedlist.printLinkedList(listaR)

        next = next.nextNode
    
def subset(L):
    listaResultado = linkedlist.LinkedList()

    print("{}")
    for i in range( linkedlist.length(L) ):
        print( linkedlist.access(L,i) )
    
    subsetRecurive(L,2)
    
    print("")
    linkedlist.printLinkedList(L) 


# L = linkedlist.LinkedList()
# linkedlist.add(L,2)
# linkedlist.add(L,1)

# linkedlist.printLinkedList(L)

# subset(L)
"""
Ejercicio 3

Escribir una función checkBST(B) que verifique que un árbol binario es un Árbol Binario de Búsqueda. Es decir que se cumple la propiedad : leftnode < currentnode < rightnode.  Implementar una versión cuya complejidad sea O(n).

"""
def checkBST(B):
    
    r=B.root
    q=LinkedList()
    enqueue(q,r)

    while length(q)!=0:
        Node=dequeue(q)
        
        if Node.leftnode!=None and Node.rightnode!=None:
            if Node.leftnode.key > Node.key or Node.rightnode.key < Node.key:
                
                return False
    
        if Node.leftnode!=None:
            enqueue(q,Node.leftnode)
        if Node.rightnode!=None:
            enqueue(q,Node.rightnode)


    return True



B = BinaryTree()
r = BinaryTreeNode()
B.root = r
r.value=2
r.key=2

C = BinaryTreeNode()
C.key =10
C.value=10
C.parent= B
r.leftnode = C


# insertB(B,1,1)
insertB(B,3,3)


print( checkBST(B) ) 

"""
Ejercicio 4
Sea BT1 y BT2 dos árboles binarios, donde BT1 es mayor que BT2. Implementar un algoritmo que determine si  BT2 es un subarbol de BT1


Ejercicio 5:
Implementar una cache de tipo LRU (Least Recently Used) de un tamaño máximo. La cache LRU debe permitir insertar y recuperar un valor a partir de una clave. En caso de superar el tamaño máximo, el elemento menos recientemente utilizado deberá ser eliminado."""
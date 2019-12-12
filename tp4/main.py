# Bruno Fuentes
# 12401

from math import*
from binarytree import*
from linkedlist import*
from queue import*
"""
Ejercicio 1:
Implementar una función isUnique(S), la cual dada una estructura de tipo String conteniendo caracteres, devuelva True or False según  corresponda, True si en la misma estructura no existen elementos repetidos, o False si existe al menos 1 elemento repetido. Nota: Es posible Implementar una versión cuya complejidad sea del orden de O(n)
"""
# ··············  FUNCION PRINCIPAL
def isUnique(listaString):    

    Aux = Array(27,0)

    for i in range(0,len(Aux)):
        Aux[i] = 0

    for i in range(0,len(listaString)):
        if listaString[i] == "A" or listaString[i] == "a":
            Aux[0] += 1
        if listaString[i] == "B" or listaString[i] == "b":
            Aux[1] += 1
        if listaString[i] == "C" or listaString[i] == "c":
            Aux[2] += 1
        if listaString[i] == "D" or listaString[i] == "d":
            Aux[3] += 1
        if listaString[i] == "E" or listaString[i] == "e":
            Aux[4] += 1
        if listaString[i] == "F" or listaString[i] == "f":
            Aux[5] += 1
        if listaString[i] == "G" or listaString[i] == "g":
            Aux[6] += 1
        if listaString[i] == "H" or listaString[i] == "h":
            Aux[7] += 1
        if listaString[i] == "I" or listaString[i] == "i":
            Aux[8] += 1
        if listaString[i] == "J" or listaString[i] == "j":
            Aux[9] += 1
        if listaString[i] == "K" or listaString[i] == "k":
            Aux[10] += 1
        if listaString[i] == "L" or listaString[i] == "l":
            Aux[11] += 1
        if listaString[i] == "M" or listaString[i] == "m":
            Aux[12] += 1
        if listaString[i] == "N" or listaString[i] == "n":
            Aux[13] += 1
        if listaString[i] == "Ñ" or listaString[i] == "ñ":
            Aux[14] += 1
        if listaString[i] == "O" or listaString[i] == "o":
            Aux[15] += 1
        if listaString[i] == "P" or listaString[i] == "p":
            Aux[16] += 1
        if listaString[i] == "Q" or listaString[i] == "q":
            Aux[17] += 1
        if listaString[i] == "R" or listaString[i] == "r":
            Aux[18] += 1
        if listaString[i] == "S" or listaString[i] == "s":
            Aux[19] += 1
        if listaString[i] == "T" or listaString[i] == "t":
            Aux[20] += 1
        if listaString[i] == "U" or listaString[i] == "u":
            Aux[21] += 1
        if listaString[i] == "V" or listaString[i] == "v":
            Aux[22] += 1
        if listaString[i] == "W" or listaString[i] == "w":
            Aux[23] += 1
        if listaString[i] == "X" or listaString[i] == "x":
            Aux[24] += 1
        if listaString[i] == "Y" or listaString[i] == "y":
            Aux[25] += 1
        if listaString[i] == "Z" or listaString[i] == "z":
            Aux[26] += 1
 
    for i in range(0,len(Aux)):
        if Aux[i] > 1:
            return True

    return False

"""
Ejercicio 2:
Dado un vector con números enteros (no repetidos)  ordenados de menor a mayor, construir un árbol de búsqueda binario con la mínima altura posible asumiendo los valores del vector como keys del árbol.
"""
def recortarArray(vect,inicio,fin):
    tam = (fin - inicio)+1
    vectorResultado = Array(tam,0)
    
    cont=0
    for i in range(inicio,fin+1,1):
        vectorResultado[cont] = vect[i]
        cont +=1

    return vectorResultado


# de una lista encola la que seria su raiz
def arbolRaiz(array,Q):
    #obtengo en indice de la raiz de este array
    indiceRaiz = trunc( len(array)/2 ) 
    enqueue(Q,array[indiceRaiz])
    return indiceRaiz

def arbolIzqDer(array,Q):
    if len(array) < 3:
        for i in range(0,len(array)): 
            enqueue(Q,array[i])
    else:
        armadoDeArbol(array,Q)

def armadoDeArbol(array,Q):
    indiceRaiz = arbolRaiz(array,Q)
    
    # arbol Izq
    arbolIzqDer( recortarArray(array,0,indiceRaiz-1) ,Q)

    # arbol Der
    arbolIzqDer( recortarArray(array,indiceRaiz+1,len(array)-1) ,Q)


# ··············  FUNCION PRINCIPAL
def arrayArbol(array):
    Q = LinkedList()

    # esta funcion arma la cola para poder armnar el arbol
    armadoDeArbol(array,Q)


    # arma la raiz del arbol 
    arbolRetorno = BinaryTree()
    nodoRaiz = BinaryTreeNode()
    aux = dequeue(Q)
    nodoRaiz.key = aux 
    nodoRaiz.value = aux
    arbolRetorno.root = nodoRaiz
    # arma el resto del arbol
    for i in range(0,length(Q)):
        aux = dequeue(Q)
        insertB(arbolRetorno,aux,aux)

    return arbolRetorno

"""
Ejercicio 3:
Dado un árbol binario, diseñar un algoritmo que cree una lista enlazada (LinkedList) con los nodos que se encuentran en cada nivel. Es decir que para un árbol con 2 niveles, el algoritmo deberá devolver 2 listas enlazadas.
"""
def BubbleSort(L):
  for i in range(length(L),0,-1):
    return BubbleSortR(L,i)

def BubbleSortR(L,pos):
  for i in range(0,pos):
    currentN=L.head
    nextN=currentN.nextNode
    p=0
    while currentN!=None and nextN!=None:
      if currentN.value>nextN.value:
        e1=currentN.value
        e2=nextN.value
        update(L,e2,p)
        update(L,e1,p+1)
      currentN=currentN.nextNode
      nextN=nextN.nextNode
      p=p+1
  return L

def printLinkedListOfLinkedList(LdL):
    currentNode = LdL.head
    while currentNode!=None:
        printLinkedList(currentNode.value)
        currentNode = currentNode.nextNode

#entra una lista vacia(Q) y una lista con los datos(L)
#sale la lista(Q) con los datos al revez y (L) queda vacia
def voltearlista(L,Q):
    index=0

    currentNode=L.head
    while currentNode!=None:
        if currentNode.nextNode==None:
            insert(Q,currentNode.value,index)
            index=index+1

            delete (L,currentNode.value)

            currentNode=L.head

        currentNode=currentNode.nextNode
        
    insert(Q,L.head.value,index)
    delete(L,L.head.value)

def CantNiveles(L, r, nivel, Val):
    if nivel > Val.head.value:
        add(Val, nivel)
    if r.leftnode!=None:
        nivel = nivel + 1
        CantNiveles(L, r.leftnode, nivel, Val)
        nivel = nivel - 1
    if r.rightnode!=None:
        nivel = nivel + 1
        CantNiveles(L, r.rightnode, nivel, Val)
        nivel = nivel - 1

def insertarListas(L, r, nivel, i, NewList ):
    if nivel == i :
        add(NewList, r.value)
    
    if r.leftnode!=None:
        nivel = nivel + 1
        
        insertarListas(L, r.leftnode, nivel, i, NewList  )
        
        nivel = nivel - 1
    
    if r.rightnode!=None:
        nivel = nivel + 1
        
        insertarListas(L, r.rightnode, nivel, i, NewList  )
        
        nivel = nivel - 1





# ··············  FUNCION PRINCIPAL
def DeArbolAlista(B):
    if B== None:
        return None
    else:
        # L lista inicial, Q lista final
        L = LinkedList()
        
        #guarla los valores de los niveles
        Val = LinkedList()
        Val1 = LinkedList()
        add(Val, 0)

        nivel = 0
        
        CantNiveles(L, B.root, nivel, Val)
        # printLinkedList(Val)
        voltearlista(Val,Val1)
        # printLinkedList(Val1)


        #en Val1 esta la cantida de niveles de arbol
        for i in range(0 , length(Val1)):
            NewList = LinkedList() 

            insertarListas(L, B.root, nivel, i, NewList )
            BubbleSort( NewList )
            
            insert(L, NewList, i)
        printLinkedListOfLinkedList(L)
        
"""
Ejercicio 4:
Implementar una función que verifique si un árbol binario está balanceado. Recordar que un árbol balanceado es aquel en el que la altura del subárbol izquierdo es igual a la del subárbol derecho. Nota: Es posible Implementar una versión cuya complejidad sea del orden de O(n)
"""
#devuelve en una lista todos los valores de los niveles
def Altura(L, r, nivel):
    add(L,nivel)
    if r.leftnode!=None:
        nivel = nivel + 1
        Altura(L, r.leftnode, nivel)
        nivel = nivel - 1
    if r.rightnode!=None:
        nivel = nivel + 1
        Altura(L, r.rightnode, nivel)
        nivel = nivel -1
    return L


# ··············  FUNCION PRINCIPAL
def balanceo(B):
    ListaAltura = LinkedList()
    ListaAltura1 = LinkedList()

    nivel = 0
    Altura (ListaAltura, B.root, nivel)
    
    voltearlista(ListaAltura, ListaAltura1)
    pop(ListaAltura1)
    ListaAltura = ListaAltura1

    referencia = ListaAltura.head.value
    #encuetra la altura maxima de la rama izquierda
    cont = 0
    currentnode = ListaAltura.head.nextNode
    while currentnode != None:
        if referencia == currentnode.value:
            RamaIzq = access(ListaAltura ,cont)
            break
        cont = cont +1
        currentnode = currentnode.nextNode

    #encuetra la altura maxima de la rama derechs
    Q = sub(ListaAltura, cont+1, length(ListaAltura))
  
    currentnode = Q.head
    RamaDer = Q.head.value
    while currentnode != None:
        if RamaDer < currentnode.value:
            RamaDer = currentnode.value
        
        currentnode = currentnode.nextNode
        
    if abs(RamaIzq - RamaDer) > 1:
        print("Desbalancedo")
    else:
        print("Balanceado")




# URL: https://repl.it/@BrunoFuentes/tp4
                                                                            
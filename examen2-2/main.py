# Bruno Fuentes
# 12401
# bruno.e.fuentes97@gmail.com


from algo1 import*
from queue import*
from linkedlist import*






def devolverNodo(L,j):
    currentNode = L.head
    cont = 0
    while currentNode!=None:
        if cont ==j:
            return currentNode

        cont +=1
        currentNode = currentNode.nextNode


def div(valor1, valor2):
    return int(valor1) // int(valor2)

def mul(valor1, valor2):
    return int(valor1) * int(valor2)

def sum(valor1, valor2):
    return int(valor1) + int(valor2)  

def res(valor1, valor2):
    return int(valor1) - int(valor2)  

def Calculate_expression(L): 
    """
    Dada una expresión matemática (almacenada en una lista de tipo LinkedList) compuesta por valores positivos enteros y operadores “+”,”-”,”*” y “/” (sin incluir paréntesis) desarrollar un algoritmo que calcule el resultado (respetando el orden de precedencia aritmética).
    """
    aux = LinkedList()
    for i in range( length(L) ):
        insert(aux, access(L,i),i )

    # divicion
    print("div")
    currentNode = aux.head
    i=0
    while currentNode!=None:
        if currentNode.value == "/":
            resultado = div( access(aux,i-1), access(aux,i+1))
            update(aux,resultado,i-1)   # cambio el valor de nodo anterior al current node
            if currentNode.nextNode.nextNode == None:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode = None
            else:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode =  nodo.nextNode.nextNode.nextNode  
            i -= 1
        i += 1
        currentNode= currentNode.nextNode

    printLinkedList(aux)




    # multiplic1acion
    print("mul")
    currentNode = aux.head
    i=0
    while currentNode!=None:
        if currentNode.value == "*":
            resultado = mul( access(aux,i-1), access(aux,i+1))
            update(aux,resultado,i-1)
            if currentNode.nextNode.nextNode == None:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode = None
            else:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode =  nodo.nextNode.nextNode.nextNode  
            i -= 1
        i += 1
        currentNode= currentNode.nextNode
        
    printLinkedList(aux)

    # suma
    print("sum")
    currentNode = aux.head
    i=0
    while currentNode!=None:
        if currentNode.value == "+":
            resultado = sum( access(aux,i-1), access(aux,i+1))
            update(aux,resultado,i-1)
            if currentNode.nextNode.nextNode == None:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode = None
            else:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode =  nodo.nextNode.nextNode.nextNode  
            i -= 1
        i += 1
        currentNode= currentNode.nextNode
        
    printLinkedList(aux)

    # resta
    print("res")
    currentNode = aux.head
    i=0
    while currentNode!=None:
        if currentNode.value == "-":
            resultado = res( access(aux,i-1), access(aux,i+1))
            update(aux,resultado,i-1)
            if currentNode.nextNode.nextNode == None:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode = None
            else:
                nodo = devolverNodo(aux,i-1)
                nodo.nextNode =  nodo.nextNode.nextNode.nextNode  
            i -= 1
        i += 1
        currentNode= currentNode.nextNode
        
    printLinkedList(aux)

    return(aux.haed.value)



L =  LinkedList()
# add(L,"3")
# add(L,"/")
add(L,"3")
add(L,"/")
add(L,"5")
add(L,"-")
add(L,"4")
add(L,"*")
add(L,"3")
add(L,"+")
add(L,"2")


# printLinkedList(L)

Calculate_expression(L)
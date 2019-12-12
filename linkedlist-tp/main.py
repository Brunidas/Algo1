# Fuentes,Bruno
# 12401


from algo1 import *
from random import *
from math import *

from linkedList import *



"""
1. Dadas las siguientes listas de elementos:
A) 24, 45, 3, 67, 89, 345, 54, 22, 3, 678
B) 46, 34, 64, 59, 12, 15, 234, 567, 12, 33
Implemente un único algoritmo en pseudocódigo que permita resolver las siguientes consignas paso a paso:
a) Llenar dos listas A y B con los elementos dados, e imprimir su contenido,
b) Crear una lista C e intercalar los elementos de las dos listas anteriores, imprimir su
contenido,
c) Buscar en la lista C todos los elementos pares de la lista A y eliminarlos, imprimir la lista C
final,
d) Generar una lista D con todos los elementos impares de C, finalmente imprimir el
contenido de D,
e) Quitarle a la lista A los elementos repetidos y añadirle al final todos los elementos de B
que se encuentren entre 50 y 100, imprimir la lista A resultante.
"""
#punto a)
listaA = LinkedList()
listaB = LinkedList()
#listaA datos
addLinkedList(listaA, 678)
addLinkedList(listaA, 3)
addLinkedList(listaA, 22)
addLinkedList(listaA, 54)
addLinkedList(listaA, 345)
addLinkedList(listaA, 89)
addLinkedList(listaA, 67)
addLinkedList(listaA, 3)
addLinkedList(listaA, 45)
addLinkedList(listaA, 24)
#listaB datos
addLinkedList(listaB, 33)
addLinkedList(listaB, 12)
addLinkedList(listaB, 567)
addLinkedList(listaB, 234)
addLinkedList(listaB, 15)
addLinkedList(listaB, 12)
addLinkedList(listaB, 59)
addLinkedList(listaB, 64)
addLinkedList(listaB, 34)
addLinkedList(listaB, 46)
#impirmir

#punto b)
listaC = LinkedList()
cont = 0
i=0
curentNodeA = listaA.head
curentNodeB = listaB.head
while(cont < lengthLinkedList(listaA)*2 ):
    insertLinkedlist(listaC, accessLinkedlist(listaA,i),cont )
    curentNodeA = curentNodeA.nextNode
    cont +=1 

    insertLinkedlist(listaC, accessLinkedlist(listaB,i),cont)
    curentNodeB = curentNodeB.nextNode
    cont +=1 

    i += 1
print('')
print('lista A')
printLinkedList(listaA)
print('')
print('lista B')
printLinkedList(listaB)
print('')
print('lista C')
printLinkedList(listaC)

#punto c)
'''listAux =LinkedList()
for i in range (0, lengthLinkedList(listaC)):
    if ( i%2==0):
        elemento = accessLinkedlist(listaC,i)
        if (elemento!= None):
            if (elemento%2 == 0 ):
                addLinkedList(listAux, elemento)

printLinkedList(listAux)
for i in range(0, lengthLinkedList(listAux) ):
    deleteLinkedlist( listaC, accessLinkedlist(listAux,i) )
print('')
print('lista C v2')
printLinkedList(listaC)'''
currentNodeC = listaC.head
i = 0
while currentNodeC != None :
    if currentNodeC.value %2 == 0:
        deleteLinkedlist(listaC,currentNodeC.value)
    currentNodeC = currentNodeC.nextNode.nextNode
print('')
print('lista C sin valores pares de A')
printLinkedList(listaC)

#punto d)
listaD = LinkedList()
cont = 0
currentNodeC = listaC.head
while(currentNodeC != None ):
    if (currentNodeC.value %2 != 0 ):
        insertLinkedlist(listaD, currentNodeC.value, cont)
        cont +=1
    currentNodeC = currentNodeC.nextNode
print('')
print('lista D')
printLinkedList(listaD)

#punto e)
    #se le sacan todos los elementos repetidos
curerentNodeGeneral = listaA.head
while (curerentNodeGeneral != None):
    currentNodeIdividual = curerentNodeGeneral.nextNode
    while( currentNodeIdividual != None):
        if (curerentNodeGeneral.value == currentNodeIdividual.value):
            deleteLinkedlist(listaA, currentNodeIdividual.value)
        currentNodeIdividual =currentNodeIdividual.nextNode
    curerentNodeGeneral = curerentNodeGeneral.nextNode
    #agregar los valores de B
currentNodeB = listaB.head
while ( currentNodeB != None ):
    if ( currentNodeB.value > 50) & (currentNodeB.value < 100 ):
        insertLinkedlist(listaA, currentNodeB.value, lengthLinkedList(listaA) )
    currentNodeB = currentNodeB.nextNode
print('')
print('lista A sin elementos')
printLinkedList(listaA)


"""
2. Desarrolle un algoritmo en pseudocódigo que permita cargar una lista en donde su campo
“value” sea igual a una estructura “Empleado” que tenga tres campos: “nombre”, “edad” y
“nroLegajo”.
a. Cargar la lista de empleados.
b. Imprimir la lista cargada.
Empleados:
Eduardo Ángel, 34, 2
Juan Carlos, 23, 5
Luis Esteban, 32, 7
Juan Carlos, 23, 5
Pedro Augusto, 40, 9
Luis Esteban, 32, 7
Pedro César, 45, 8
Eduardo Ángel, 34, 2
Luis Esteban, 32, 7
"""
#punto a)
class Empleados():
    nombre=None;
    edad = None;
    nroLegajo = None;
empleadoA = Empleados()
empleadoB = Empleados()
empleadoC = Empleados()
empleadoD = Empleados()
empleadoE = Empleados()
empleadoF = Empleados()
empleadoG = Empleados()
empleadoH = Empleados()
empleadoI = Empleados()
#nombre
empleadoA.nombre = "Eduardo Ángel"
empleadoB.nombre = "Juan Carlos"
empleadoC.nombre = "Luis Esteban"
empleadoD.nombre = "Juan Carlos"
empleadoE.nombre = "Pedro Augusto"
empleadoF.nombre = "Luis Esteban"
empleadoG.nombre = "Pedro César"
empleadoH.nombre = "Eduardo Ángel"
empleadoI.nombre = "Luis Esteban"
#edad
empleadoA.edad = 34
empleadoB.edad = 23
empleadoC.edad = 32
empleadoD.edad = 25
empleadoE.edad = 40
empleadoF.edad = 32
empleadoG.edad = 45
empleadoH.edad = 34
empleadoI.edad = 32
#nroLegajo
empleadoA.nroLegajo = 2 
empleadoB.nroLegajo = 5
empleadoC.nroLegajo = 7
empleadoD.nroLegajo = 5
empleadoE.nroLegajo = 9
empleadoF.nroLegajo = 7
empleadoG.nroLegajo = 8
empleadoH.nroLegajo = 2
empleadoI.nroLegajo = 7
#nodos
nodoA = empleadoA 
nodoB = empleadoB 
nodoC = empleadoC 
nodoD = empleadoD 
nodoE = empleadoE 
nodoF = empleadoF 
nodoG = empleadoG 
nodoH = empleadoH 
nodoI = empleadoI 
#lista
listaEmpleados = LinkedList()
#agrenar nodos
addLinkedList(listaEmpleados, nodoI)
addLinkedList(listaEmpleados, nodoH)
addLinkedList(listaEmpleados, nodoG)
addLinkedList(listaEmpleados, nodoF)
addLinkedList(listaEmpleados, nodoE)
addLinkedList(listaEmpleados, nodoD)
addLinkedList(listaEmpleados, nodoC)
addLinkedList(listaEmpleados, nodoB)
addLinkedList(listaEmpleados, nodoA)

#punto b)
    #funcion valida para imprimir la lista de empleados
def printEmpleados(listaEmpleados):
    curerentNodeEmpleados = listaEmpleados.head
    while( curerentNodeEmpleados!=None ):
        print(
            str(curerentNodeEmpleados.value.nombre) + ", "+
            str(curerentNodeEmpleados.value.edad) +  ", "+
            str(curerentNodeEmpleados.value.nroLegajo) )
        curerentNodeEmpleados = curerentNodeEmpleados.nextNode
    #llamdos a la funcion
print('')
print("Datos:")
printEmpleados(listaEmpleados)

"""
3. Para el ejercicio anterior:
a) Eliminar los elementos donde nroLegajo se encuentren duplicados.
b) Agregar antes del legajo número 7 el siguiente: Ernesto Andrés, 55, 6.
c) Mover el legajo 9 luego del legajo 8.
d) Imprimir la lista resultante.
"""

#punto a)
curerentNodeEmpleados = listaEmpleados.head
while (curerentNodeEmpleados != None):

    currentNodeLegajo = curerentNodeEmpleados.nextNode
    while( currentNodeLegajo != None):
        if (curerentNodeEmpleados.value.nroLegajo == currentNodeLegajo.value.nroLegajo):
            deleteLinkedlist(listaEmpleados, currentNodeLegajo.value)
        currentNodeLegajo =currentNodeLegajo.nextNode

    curerentNodeEmpleados = curerentNodeEmpleados.nextNode

'''print('')
print("Datos actulizados:")
printEmpleados(listaEmpleados)'''

#punto b)
newEmpleado = Empleados()
newEmpleado.nombre = "Ernesto Andrés"
newEmpleado.edad = 55
newEmpleado.nroLegajo = 6

cont = 0
curerentNodeEmpleados = listaEmpleados.head
while( curerentNodeEmpleados != None):
    if ( curerentNodeEmpleados.value.nroLegajo == 7):
        insertLinkedlist(listaEmpleados,newEmpleado, cont)
        break
    curerentNodeEmpleados = curerentNodeEmpleados.nextNode
    cont += 1

'''print('')
print("Nuevos Empleado:")
printEmpleados(listaEmpleados)
'''
#punto c) 
empleadoAuxNL9 = Empleados()
empleadoAuxNL8 = Empleados()

curerentNodeEmpleados = listaEmpleados.head
while( curerentNodeEmpleados != None):    
    if ( curerentNodeEmpleados.value.nroLegajo == 9):
        empleadoAuxNL9.nombre = curerentNodeEmpleados.value.nombre
        empleadoAuxNL9.edad = curerentNodeEmpleados.value.edad
        empleadoAuxNL9.nroLegajo = curerentNodeEmpleados.value.nroLegajo

        indice9 = searchLinkedlist(listaEmpleados, curerentNodeEmpleados.value)

    if ( curerentNodeEmpleados.value.nroLegajo == 8):
        empleadoAuxNL8.nombre = curerentNodeEmpleados.value.nombre
        empleadoAuxNL8.edad = curerentNodeEmpleados.value.edad
        empleadoAuxNL8.nroLegajo = curerentNodeEmpleados.value.nroLegajo

        indice8 = searchLinkedlist(listaEmpleados, curerentNodeEmpleados.value)
    curerentNodeEmpleados = curerentNodeEmpleados.nextNode

updateLinkedlist(listaEmpleados, empleadoAuxNL8, indice9)
updateLinkedlist(listaEmpleados, empleadoAuxNL9, indice8)

print('')
print('Lista final:')
printEmpleados(listaEmpleados)



# URL:
# https://repl.it/@BrunoFuentes/linkedlist-tp
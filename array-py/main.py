from algo1 import *
from random import *
from math import *
from array import *

def valoresVector(vect):
    for i in range(len(vect)):
        vect[i] = randint(1, 3)
    return vector

#search
#datos
n = 5
vector = Array(n,0)
vector = valoresVector(vector)
print('')
print('-------------------------------------')
print('search\n')
print(vector)
print('vector\n')
#llamado
elementoABuscar = 3
print('elemento a buscar: '+str(elementoABuscar)+"\n" )
print("el elemento esta en la posición: " + str(search(vector,elementoABuscar)) )



#insert
#datos

n = 5
vector = Array(n,0)

vector[0] = 10
vector[1] = 20
vector[2] = 30
vector[3] = None
vector[4] = None

print('')
print('-------------------------------------')
print('insert\n')
print(vector)
print('vector\n')
#llamado
elemento = 999
posicion = 2
print("elemento a insertar:"+str(elemento)+"\nposicion a insertar:"+str(posicion)+"\n" )
print("el elemento se incertado en la posicion: " + str( insert(vector,elemento,posicion) ) )




#delete
#datos
n = 5
vector = Array(n,0)

vector[0] = 10
vector[1] = 20
vector[2] = 30
vector[3] = 40
vector[4] = 50

print('')
print('-------------------------------------')
print('delete\n')
print(vector)
print('vector\n')
#llamado 10
elemento = 10
print('elemento a eliminar:'+str(elemento) ) 
print('el elemento a elimnar estaba en la posicion:'+str(delete(vector,elemento) ))


#legth
#datos
n = 5
vector = Array(n,0)
vector = valoresVector(vector)
print('')
print('-------------------------------------')
print('length\n')
print(vector)
print('vector\n')
#llamado
print( 'elementos activos de array:' +str(length(vector)) ) 



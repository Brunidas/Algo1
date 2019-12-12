# FUENTES, Bruno
# 12401


from algo1 import* 

def createSet(vect):
    '''
    Create_Set(Array):
    Descripción: Crea un TAD de tipo Set a partir de un arreglo recibido como
    parametro.
    Precondición: La operación debe garantizar que no hay elementos duplicados
    en los arreglos.
    Entrada: el Arreglo sobre el cual se quiere construir el TAD Set
    Salida: Un Array que representa el TAD Set
    '''
    #cunado se repite un valor lo remplaza por None
    for i in range( len(vect) ):
        aux = vect[i]

        for j in range( len(vect)):
            if (i != j):
                if (aux == vect[j]):
                    vect[j] = None   
    # obtiene la dimencion del conjunto
    dimVect = 0
    for i in range(len(vect)):
        if (vect[i] != None):
            dimVect += 1
    #declaro en nuevo conjunto como array
    newVect = Array( dimVect,0)
    
    # coloco los valores distintos de None en newVect
    cont = 0
    for i in range( len(vect)):
        if (vect[i] != None):
            newVect[cont] = vect[i]
            cont += 1 

    #devuelve el conjunto 
    return newVect




def union(vector1 ,vector2):
    '''
    Union(Array S,Array T):
    Descripción: Aplica la operación UNIÓN sobre los conjuntos S y T.
    Precondición: La operación debe garantizar que no hay elementos duplicados
    en los arreglos.
    Entrada: Dos arreglos que representan los Sets S y T
    Salida: Un Array que representa un nuevo TAD Set
    '''
    #los convierte a conjuntos
    vector1 = createSet(vector1)
    vector2 = createSet(vector2)

    dimNewVector = len(vector1) +len(vector2)
    # vector de dimension de la suma de los 2 vecrtores
    newVector = Array(dimNewVector ,0)

    #agrega vector1 a newVector
    j = 0
    for i in range(len(vector1) ):
        newVector[i] = vector1[i]
        j += 1
    #agrega vector2 a newVector
    cont = 0
    for i in range(len(newVector)):
        if (newVector[i] == None ):
            newVector[i] = vector2[cont]
            cont += 1

    #lo convierte a conjunto
    newVector = createSet(newVector)
    
    #devuelve el conjunto
    return newVector


def intersection(vector1, vector2):
    '''
    Intersection(Array S,Array T):
    Descripción: Aplica la operación INTERSECCIÓN sobre los conjuntos S y T.
    Precondición: La operación debe garantizar que no hay elementos duplicados
    en los arreglos.
    Entrada: Dos arreglos que representan los Sets S y T
    Salida: Un Array que representa un nuevo TAD Set
    ''' 
    #los convierte a conjuntos
    vector1 = createSet(vector1)
    vector2 = createSet(vector2)

    dimNewVector = len(vector1) +len(vector2)
    # vector de dimension de la suma de los 2 vecrtores
    newVector = Array(dimNewVector ,0)

    # encuentro los valores iguales y los guardo en newVecor
    cont = 0
    for i in range( len(vector1) ):
        valorACompar = vector1[i]
        for j in range( len(vector2) ):
            if ( valorACompar == vector2[j] ):
                newVector[cont] = valorACompar
                cont += 1
    #lo convierte a conjunto
    newVector = createSet(newVector)

    #devuelve el conjunto
    return newVector




def difference(vector1, vector2):
    '''
    Difference(Array S, Array T):
    Descripción: Aplica la operación DIFERENCIA sobre los conjuntos S y T.
    Precondición: La operación debe garantizar que no hay elementos duplicados
    en los arreglos.
    Entrada: Dos arreglos que representan los Sets S y T
    Salida: Un Array que representa un nuevo TAD Set
    '''
    
    # vector1 - vector2
    
    
    #los convierte a conjuntos
    vector1 = createSet(vector1)
    vector2 = createSet(vector2)

    # vector de dimension de la suma de los 2 vectores
    dimNewVector = len(vector1) +len(vector2)

    auxVector = intersection(vector1, vector2)
    
    newVector = vector1
    # los valores que son iguales a los de la intersection se igualan a None
    for i in range( len(auxVector) ):
        valorACompar = auxVector[i]
        for j in range ( len(newVector) ):
            if ( valorACompar == newVector[j] ):
                newVector[j] =None
    #lo convierte a conjunto
    newVector = createSet(newVector)

    #devuelve el conjunto
    return newVector


#URL 
# https://repl.it/@BrunoFuentes/TP1
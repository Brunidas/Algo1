# FUENTES, Bruno
# 12401


from algo1 import*
from random import  *
from math import *
from Set import *
#from colorama import *



def valores(vect):
    for i in range(len(vect)):
        vect[i] = randint(-5,5)
    print(vect)
    return






#muestra en pantalla toda la parte uno practico
def parteUno():
    # PARTE 1: Arreglos y Matrices
    '''
    1. Elaborar un algoritmo que lea un vector, busque el mayor elemento en valor absoluto y
    muestre el resultado.
    '''
    print("")
    #print(Fore.WHITE+Back.BLUE+"PARTE #1"+Back.RESET)
    print('PARTE #1\n')
    print('#########################################################')
    print('punto 1\n')


    def mayorValor(vect):
        mayor = 0
        for i in range(len(vect)):
            if mayor < abs(vect[i]):
                mayor = abs(vect[i])
        print('El mayor valor encontrado en valor absoluto es:', mayor)
    



    # se define al vector
    n = 5
    vector = Array(n,0)

    #se le agregar valores 
    valores(vector)
    print('vector \n')



    #funcion
    mayorValor(vector)

    '''
    2. Elaborar un algoritmo que lea dos vectores, verifique si tienen la misma dimensión y los sume
    almacenándolos en un nuevo vector. Calcule la norma cuadrática de este último vector.
    Muestre el vector resultado y su norma cuadrática.
    '''
    print("")
    print('#########################################################')
    print('punto 2\n')



    def normaCuadrica(vect):
        resultado = 0
        for i in range( len(vect) ):
            resultado += vect[i]**2
        return sqrt( resultado )



    def sumVectores(vect1, vect2):
        if ( len(vect1) == len(vect2) ):
            vectorResultado = Array( len(vect1), 0)        
            for i in range( len(vect1) ):
                vectorResultado[i] = vect1[i] + vect2[i]
            print(vectorResultado)
            print('vector resultado\n')
            print('Norma Cuadrica del vector es:', normaCuadrica( vectorResultado ))
        else:
            print('Los vectores tienen dimensiones distintas')
            return None




    #se definen los vectores
    dimVect1 = 5;
    dimVect2 = 5;
    vector1 = Array(dimVect1, 0)
    vector2 = Array(dimVect2, 0)

    #funcion definida en la parte de arriba
    valores(vector1)
    print('vector 1\n')
    valores(vector2)
    print('vector 2\n')




    #funcion
    sumVectores(vector1, vector2)
    """
    3. Elaborar un algoritmo que lea dos vectores, verifique si tienen la misma dimensión y obtenga
    el producto escalar de los mismos. Muestre el resultado.
    """
    print("")
    print('#########################################################')
    print('punto 3\n')




    def productoEscalar(vect1, vect2):
        if ( len(vect1) == len(vect2) ):
            resultado = 0
            for i in range( len(vect1) ):
                resultado += (vect1[i] * vect2[i]) 
            
            print('El producto escalar es:',resultado )
        else:
            print('Los vectores tienen dimensiones distintas')




    #se definen los vectores
    dimVect1 = 5;
    dimVect2 = 5;
    vector1 = Array(dimVect1, 0)
    vector2 = Array(dimVect2, 0)

    #funcion definida en la parte de arriba
    valores(vector1)
    print('vector 1\n')
    valores(vector2)
    print('vector 2\n')




    #funcion
    productoEscalar(vector1, vector2)
    """
    4. Elaborar un algoritmo que lea una matriz y un vector, y que verifique si es posible la
    multiplicación. En el caso de ser posible realice la operación correspondiente, caso contrario
    muestre el mensaje “dimensiones incorrectas”.
    """
    print("")
    print('#########################################################')
    print('punto 4\n')

    def valoresMatriz( matrix, M, N ):
        for i in range( M ):
            for j in range ( N ):
                matrix[i][j] = randint(-3,3)
            print(matrix[i])
        return



    def productoMatrizVector(vect, mtrx):
        if (len(vect) == len(mtrx[1])):
            vectorResultado = Array( len(vect),0)
            for i in range(len(vect)):
                #obtiene los componetes individualmete
                sumaParcial = 0
                for j in range(len( mtrx[i]) ):
                    sumaParcial += (mtrx[i][j] * vect[j])
                #los agrega al vector resultado
                vectorResultado[i] = sumaParcial
            print(vectorResultado)
            print('vector resultado')
        else:
            print('“dimensiones incorrectas”')




    # se define una matriz de matriz de mxn
    dimMatrizM = 3
    dimMatrizN = 3
    matriz = Array(dimMatrizM, Array(dimMatrizN, 0) )
    valoresMatriz(matriz, dimMatrizM, dimMatrizN )
    print('matrix\n')

    #se define los vectores
    dimVector = 3
    vector = Array( dimVector, 0)

    #funcion definida en la parte de arriba
    valores(vector)
    print('vector\n')



    #funcion
    productoMatrizVector(vector, matriz)
    """
    5. Elaborar un algoritmo que lea dos matrices, calcule la diferencia de las mismas y almacene el
    resultado en una tercer matriz.
    """
    print("")
    print('#########################################################')
    print('punto 5\n')


    def printMatrix(matrix):
        for i in range( len(matrix) ):
            print(matrix[i])



    def restarMatriz(mtrx1, mtrx2):
        if ( len(mtrx1)==len(mtrx2) & len(mtrx1[1])==len(mtrx2[1])):
            mtrx3 = Array(len(mtrx1), Array(len(mtrx1[1]), 0) )
            for i in range (len(mtrx1)):
                for j in range(len(mtrx1[1])):
                    mtrx3[i][j] = mtrx1[i][j] - mtrx2[i][j]
                # print(mtrx3[i])
            printMatrix(mtrx3)
            print("matriz resultado")
        else:
            print('“dimensiones incorrectas”')




    # matriz de mxn
    dimMatrizM = 3
    dimMatrizN = 3
    matrizA = Array(dimMatrizM, Array(dimMatrizN, 0) )

    #matriz de jxk
    dimMatrizJ = 3
    dimMatrizK = 3
    matrizB = Array(dimMatrizJ, Array(dimMatrizK, 0) )

    # definida en el punto 4
    valoresMatriz(matrizA, dimMatrizM, dimMatrizN )
    print("matriz A\n")
    valoresMatriz(matrizB, dimMatrizJ, dimMatrizK )
    print("matriz B\n")




    #funcion
    restarMatriz(matrizA,matrizB)
    """
    6. Elaborar un algoritmo que lea dos matrices, calcule su producto y almacene el resultado en
    una tercer matriz. Verifique si esta última matriz es estrictamente diagonal dominante por
    filas.
    """
    print("")
    print('#########################################################')
    print('punto 6\n')


    def productoFilaColumna(fila, columna):
        resultado = 0
        for i in range(len(fila) ):
            resultado += ( fila[i] * columna[i] ) 
        return resultado



    # nColumna --> numero de columna 
    def vectorColumna(matriz, nColumna, dimColumna):
        nuevoVector =  Array(dimColumna, 0)
        cont = 0
        for i in range( len(matriz) ):
            for j in range( len(matriz[1]) ):    
                if ( j==nColumna ):
                    nuevoVector[cont] = matriz[i][j]
                    cont += 1
        return nuevoVector




    def productoMatriz(mtrx1, mtrx2):
        #el n de columnas de mtrx1 debe ser igual al numero de fila de mtrx2
        if (len(mtrx1[0]) == len(mtrx2) ):
            #debe tener las columnas de mtrx2 debe ser igual al numero de fila de mtrx1
            matrizResultado = Array(len(mtrx1), Array(len(mtrx2[1]), 0) )
            for i in range(len(matrizResultado) ):
                for j in range(len(matrizResultado[1]) ):
                    vectorAuxiliar = vectorColumna(mtrx2, j, len(matrizResultado[1]))
                    matrizResultado[i][j] = productoFilaColumna(mtrx1[i], vectorAuxiliar ) 

            #definida en el punto 5
            printMatrix(matrizResultado)
            print("matriz resultado\n")

            return matrizResultado
        else:
            print('“dimensiones incorrectas”')




    #suma de los valores absolutos en si contar el valor de la diagonal principal 
    def sumaAbs(mtrx, fila ):
        resultado = 0
        for i in range(len(mtrx)):
            if ( i != fila ):
                resultado += abs(mtrx[fila][i] )
        return resultado




    def MatricesDeDiagonalEstrictamenteDominante(mtrx):
        cont = 0 
        for i in range(len(mtrx)):
            for j in range(len(mtrx)):
                if ( i==j ):
                    if (abs(mtrx[i][j]) > sumaAbs(mtrx,i ) ):
                        cont += 1
        if ( cont == len(mtrx) ):
            print('La matriz de diagonal estrictamente dominante')
        else:
            print('La matriz de diagonal no estrictamente dominante')





    # matriz de mxn
    dimMatrizM = 2
    dimMatrizN = 2

    #matriz de jxk
    dimMatrizJ = 2
    dimMatrizK = 2

    #definir las matrices
    matrizA = Array(dimMatrizM, Array(dimMatrizN, 0) )
    matrizB = Array(dimMatrizJ, Array(dimMatrizK, 0) )

    # definida en el punto 4
    valoresMatriz(matrizA, dimMatrizM, dimMatrizN )
    print("matriz A\n")
    valoresMatriz(matrizB, dimMatrizJ, dimMatrizK )
    print("matriz B\n")



    # funciones
    matrizResultado = productoMatriz(matrizA, matrizB)
    MatricesDeDiagonalEstrictamenteDominante(matrizResultado)

    """
    7. Elaborar un algoritmo que lea una matriz y determine si es triangular superior. En caso
    afirmativo el algoritmo debe calcular el determinante de dicha matriz.
    """
    print("")
    print('#########################################################')
    print('punto 7\n')



    def NoMatrizTriangularS():
        print('No es matriz triangular superior')




    # TS es de triangular superior
    # cartidadDeCeros cuenta la cantidad ceros que estan en la posicion correcta 
    def cartidadDeCerosTS(mtrx):
        resultado = 0
        for i in range( len(mtrx)):
            for j in range( len(mtrx)):
                if ( j < i):
                    if (mtrx[i][j] == 0):
                        resultado += 1
        return resultado 





    def detMatrizTriangular(mtrx):
        det = 1
        for i in range( len(mtrx)):
            for j in range( len(mtrx)):
                if ( i==j ):
                    det *= (mtrx[i][j])
        return det





    def matrizTriangularSuperior(matriz):
        if ( len(matriz) == len(matriz[0])):
            ceros = cartidadDeCerosTS(matriz)
            
            # cont cuenta la cantidad de elementos que debajo de la diagonal superior
            cont = 0
            for i in range( len(matriz) ):
                for j in range( len(matriz)):
                    if (i < j):
                        cont += 1
            if (ceros == cont):
                print('Es matriz triangular superior\n')
                det = detMatrizTriangular(matriz)
                print('El determinante de la matriz es: '+ str(det))
            else:
                NoMatrizTriangularS()
        else:
            NoMatrizTriangularS()






    # matriz de mxn
    dimMatrizM = 2
    dimMatrizN = 2

    #define la matriz
    matriz = Array(dimMatrizM, Array(dimMatrizN, 0) )

    # definida en el punto 4
    valoresMatriz(matriz, dimMatrizM, dimMatrizN )
    print('matrix\n')

    matriz[1][0] = 0
    #definida en el punto 5
    printMatrix( matriz ) 





    # funcion
    matrizTriangularSuperior( matriz )
    """
    8. Elaborar un algoritmo que lea una matriz y determine si es triangular inferior. En caso
    afirmativo el algoritmo debe calcular la matriz transpuesta de la misma.
    """
    print("")
    print('#########################################################')
    print('punto 8\n')



    def NoMatrizTriangularI():
        print('No es matriz triangular inferior')



    # TI es de triangular superior
    # cartidadDeCeros cuenta la cantidad ceros que estan en la posicion correcta 
    def cartidadDeCerosTI(mtrx):
        resultado = 0
        for i in range( len(mtrx)):
            for j in range( len(mtrx)):
                if (i<j):
                    if (mtrx[i][j] == 0):
                        resultado += 1
        return resultado 





    def trasponerMatriz( matrix ) :
        filas = len(matrix[0])
        columnas = len(matrix)

        newMatrix = Array(filas, Array(columnas, 0) )
        for i in range( len(matrix) ):
            for j in range( len(matrix[0]) ):
                newMatrix[j][i] = matrix[i][j]
        printMatrix(newMatrix)





    def matrizTriangularInferior(matriz):
        if ( len(matriz) == len(matriz[0])):
            ceros = cartidadDeCerosTI(matriz)

            cont = 0
            for i in range( len(matriz) ):
                for j in range( len(matriz)):
                    if (i < j):
                        cont += 1
            if (ceros == cont):
                print('Es matriz triangular inferior\n')
                trasponerMatriz( matriz )
                print('matriz transpuesta')
            else:
                NoMatrizTriangularI()
        else:
            NoMatrizTriangularI()




    # matriz de mxn
    dimMatrizM = 2
    dimMatrizN = 2

    matriz = Array(dimMatrizM, Array(dimMatrizN, 0) )

    # definida en el punto 4
    valoresMatriz(matriz, dimMatrizM, dimMatrizN )
    print('matrix\n')

    matriz[0][1] = 0
    printMatrix( matriz ) 





    #funcion
    matrizTriangularInferior( matriz )



#muestra en pantalla toda la parte dos practico
def parteDos():

    # PARTE 2
    print("")
    print('PARTE #2')
    print('(Set.py)\n')
    print('#########################################################')
    print('Create Set\n')
    n=10
    vector = Array(n,0)
    valores(vector)
    print('vector\n')
    conjunto = createSet(vector)
    print(conjunto)
    print('conjunto\n')
    

    print('#########################################################')
    print('Union\n')
    n=10
    vector1 = Array(n,0)
    valores(vector1)
    print('vector1 \n')

    n=10
    vector2 = Array(n,0)
    valores(vector2)
    print('vector2 \n')

    conjunto1 = createSet(vector1)
    print(conjunto1)
    print('conjunto1\n')


    conjunto2 = createSet(vector2)
    print(conjunto2)
    print('conjunto2\n')


    conjuntoResultado = union(vector1, vector2)
    print(conjuntoResultado)
    print('conjunto resultado\n')
    

    print('#########################################################')
    print('Intersection\n')
    n=10
    vector1 = Array(n,0)
    valores(vector1)
    print('vector1 \n')

    n=10
    vector2 = Array(n,0)
    valores(vector2)
    print('vector2 \n')

    conjunto1 = createSet(vector1)
    print(conjunto1)
    print('conjunto1\n')


    conjunto2 = createSet(vector2)
    print(conjunto2)
    print('conjunto2\n')


    conjuntoResultado = intersection(vector1, vector2)
    print(conjuntoResultado)
    print('conjunto resultado\n')
    


    print('#########################################################')
    print('Difference\n')
    n=10
    vector1 = Array(n,0)
    valores(vector1)
    print('vector1 \n')

    n=10
    vector2 = Array(n,0)
    valores(vector2)
    print('vector2 \n')

    conjunto1 = createSet(vector1)
    print(conjunto1)
    print('conjunto1\n')


    conjunto2 = createSet(vector2)
    print(conjunto2)
    print('conjunto2\n')


    conjuntoResultado = difference(vector1, vector2)
    print(conjuntoResultado)
    print('conjunto resultado\n')



#llamados a las partes de programa

parteUno()
print('\n')
print('\n')
print('\n')
parteDos()




#URL 
# https://repl.it/@BrunoFuentes/TP1

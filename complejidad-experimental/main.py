# FUENTES, Bruno
# 12401


from algo1 import*
import time

'''
Intervalo de [0,100] paso 10
----------------------------------------------------------------------
'''
# Algoritmo inútil que resta billetes de 100,10 y 1 a un monto dado.
def entrega_billetes_2(monto):
        start = time.time() 
        billete=100
        inc=0
        billete_actual=billete/(10**inc)
        while (monto>0):
                if monto >= billete_actual:
                        monto=monto-billete_actual
                        
                else:
                        inc=inc+1
                        billete_actual=billete/(10**inc)
                        
        end = time.time() 
        return(end - start)

for i in range(0,110,10):
    resultado = entrega_billetes_2(i)
    print(resultado)
print("resultado final "+str(resultado)+"\n")

'''
----------------------------------------------------------------------
Intervalo de [100,1000] con paso 100
'''

for i in range(100,1100,100):
    resultado = entrega_billetes_2(i)
    print(resultado)
print("resultado final "+str(resultado)+"\n")

'''
----------------------------------------------------------------------
Intervalo de [1000,10000] con paso 1000
'''
for i in range(1000,11000,1000):
    resultado = entrega_billetes_2(i)
    print(resultado)
print("resultado final "+str(resultado)+"\n")


'''
----------------------------------------------------------------------
Intervalo de [10000,100000] con paso 10000
'''
for i in range(10000,110000,10000):
    resultado = entrega_billetes_2(i)
    print(resultado)
print("resultado final "+str(resultado)+"\n")


'''
----------------------------------------------------------------------
Intervalo de [100000,1000000] con paso 100000
'''
for i in range(100000,1100000,100000):
    resultado = entrega_billetes_2(i)
    print(resultado)
print("resultado final "+str(resultado)+"\n")
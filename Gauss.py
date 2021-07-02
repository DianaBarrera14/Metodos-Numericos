#Programe  el  método  de  sustitución  regresiva.
# Analice  el  número  de operaciones del algoritmo
# para matrices de tamaño 3×3.

#DIANA FABIOLA BARRERA GALLO

#Importo la librería para resolver la matriz
import numpy as np
#Ingresamos los elementos de la matriz
A=np.array ([[ 2,1,-1],
              [ -3,-1,2],
              [ -2,1,2]])

b=np.array ([8,-11,-3])
print('La matriz ingresada es:')
print(A,b)
print('---------------------------------------------')

N=len(b)
x=np.zeros(N)
#Estructura repetitiva para tomar un pivote y el resto de
#elementos se transforman en ceros, es decir, realizar
#operaciones elementales por fila.
for i in range(N-1):
    b[i]=b[i]/A[i][i]
    A[i]=A[i]/A[i][i]
    print(A,b)
    print('---------------------------------------------')
    for k in range (i+1,N):
     b[k] = b[k]-A[k][i]*b[i]

     A[k] = A[k]-A[k][i]*A[i]
    print(A,b)
    print('---------------------------------------------')

i=N-1
b[i]=b[i]/A[i][i]
A[i]=A[i]/A[i][i]
#Imprime matriz resultante
print('La matriz reducida por el método de Gauss es:')
print(A,b)

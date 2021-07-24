import numpy as np
n=4
#Ingresamos la matriz
A=np.array([[6,0,0,0], [3,6,0,0], [4,-2,7,0],[5,-3,9,21]])
b= ([12,-12,14,-2])
#Creamos una matriz de ceros
x=np.zeros([n])
x[0]=b[0]/A[0,0]
#Recorrer el arreglo con ciclos repetitivos
for i in range(1,n,1):
    sAx=0
    for j in range(0,i,1):
        sAx=sAx+A[i,j]*x[j]
        x[i]= (b[i]-sAx)/A[i,i]
#Matriz transpuesta
xTrans=np.array([x]).T
#Imprimir resultados
print('La matriz ingresada es:', A,b)
print('La solución para el sistema de ecuaciones lineales para X1, X2, X3, X4 es: ', xTrans)

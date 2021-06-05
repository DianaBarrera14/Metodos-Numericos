# 2. Desarrolle en Python un programa para calcular la inversa de matrices de dimensión 2 × 2.
# No olvide colocar comentarios en su programa. No busque el programa en internet.

# DIANA FABIOLA BARRERA GALLO

#Importamos la librería para manejar funciones matemáticas
import numpy as np

# Creamos un array con los valores de la matriz
b=np.array([[7,8],[1,4]])

# Definimos un método para obtener el determinante de la matriz
def obtenerDeterminante(b):
    det=b[0][0]*b[1][1]-b[0][1]*b[1][0]
    return det

# Definimos un método para obtener la matriz adjunta
def matrizAdjunta(b):
    matAux=b
    aux=matAux[0][0]
    matAux[0][0]=matAux[1][1]
    matAux[1][1]=aux

    aux=matAux[0][1]
    matAux[0][1]=-matAux[1][0]
    matAux[1][0]=-aux
    return matAux

# Finalmente mandamos a imprimir los resultados obtenidos
print("La matriz original es: ")
print(b)
print("El determinante de la matriz es: ")
det=obtenerDeterminante(b)
print(det)

print("La matriz adjunta de la transpuesta es: ")
adj=matrizAdjunta(b.T)
print (adj)

print("La matriz inversa es: ")
print((1/det)*adj)




import numpy as np
filas = int(input("Ingrese el numero de filas: "))
colum= int(input("Ingrese el numero de columnas: "))

matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(colum):
        val=float(input('Elemento Fila{}, Columna{}: '.format(i+1, j+1)))
        matriz[i].append(val)

print()
for filas in matriz:
    print('[', end=' ')
    for elem in filas:
        print('{:8.2f}'.format(elem), end=' ')
    print(']')
print()

np.linalg.norm(matriz,'fro')
np.linalg.cond(matriz,'fro')
print('Norma Frobenius de la matriz ingresada:')
print(np.linalg.norm(matriz,'fro'))
print()
print('Numero de condiciones:')
print(np.linalg.cond(matriz,'fro'))




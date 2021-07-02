from numpy import array, zeros, dot, diag
# Ingreso de matrices
A = array([[4., -1., 0., -1.], [-1., 4., -1., 0.], [-1., 0., -1., 4.], [0., -1., 4., -1.]])
B = array([[30.], [60.], [70.], [40.]])

def GEPP(A, b):
    # Eliminacion gaussiana sin pivote
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)

    for k in range(n - 1):

        for row in range(k + 1, n):
            multiplier = A[row][k] / A[k][k]

            A[row][k] = multiplier
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier * A[k][col]
            b[row] = b[row] - multiplier * b[k]
    x = zeros(n)
    k = n - 1
    x[k] = b[k] / A[k, k]
    while k >= 0:
        x[k] = (b[k] - dot(A[k, k + 1:], x[k + 1:])) / A[k, k]
        k = k - 1
    return x

print('LA MATRIZ INGRESADA ES:')
print(A, B)
Aug = GEPP(A, B)
print('LAS SOLUCIONES PARA EL SISTEMA DE ECUACIONES '
      'RESPECTIVAMENTE SON (X1, X2, X3, X4):')
print(Aug)
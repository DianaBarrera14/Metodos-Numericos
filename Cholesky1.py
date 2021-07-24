from math import sqrt
import pprint
def cholesky(A):
    n = len(A)
# Creamos una matriz de ceros
    L = [[0.0] * n for i in range(n)]
#Descomposición de Cholesky
    for i in range(n):
        for k in range(i + 1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))

            if (i == k):  # Elementos de la diagonal
                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L

A = [[4, 6, 10], [6, 25, 19], [10, 19, 62]]
L = cholesky(A)

print ('A:')
pprint.pprint(A)

print('L:')
pprint.pprint(L)


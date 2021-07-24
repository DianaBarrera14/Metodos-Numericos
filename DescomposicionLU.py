import pprint
import numpy as np
import scipy.linalg

A=np.array([[6,0,0,0], [3,6,0,0], [4,-2,7,0],[5,-3,9,21]])
b= ([12,-12,14,-2])
P, L, U = scipy.linalg.lu(A)
print ('MATRIZ INGRESADA')
print ('A:')
pprint.pprint(A)
print ('b:')
pprint.pprint(b)
print ('--------------------------------------------------------------------')
print ('Matriz IDENTIDAD')
print ('P:')
pprint.pprint(P)
print ('--------------------------------------------------------------------')
print('DESCOMPOSICIÓN L * U')
print ('L:')
pprint.pprint(L)

print ('U:')
pprint.pprint(U)
print ('--------------------------------------------------------------------')
print('COMPROBACIÓN: L * U = A')
c= np.dot(L,U)
print(c)

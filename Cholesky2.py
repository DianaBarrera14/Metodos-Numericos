import pprint
import scipy.linalg
import numpy as np
A = scipy.array= [[4, 6, 10], [6, 3, 19], [10, 19, 62]]
L = scipy.linalg.cholesky(A, lower=True)
U = scipy.linalg.cholesky(A, lower=False)

print ('A:')
pprint.pprint(A)

print('L:')
pprint.pprint(L)

print('U:')
pprint.pprint(U)

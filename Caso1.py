import numpy as np
n=100
a=0.5*np.ones([100])
b=2*np.ones([100])
b[0]=1.5
b[99]=1.5
c=0.5*np.ones([100])
d=np.ones([100])

def tridiag(n,d,a,c,b):
    x = np.zeros(n)
    for i in range(1,n-1):
        mult = a[i-1]/d[i-1]
        d[i]-= mult*c[i-1]
        b[i] -= mult * b[i-1]
        print(d)
        x[n-1]=b[n-1]/d[n-1]
        for i in range (n-2,-1,-1):
            x[i]=(b[i]-c[i]*x[i+1]/d[i])
        return x
print('Subdiagonal')
print(a)
print('Terminos independientes')
print(b)
print('Superdiagonal')
print(c)
print('Diagonal')
print(d)
print('Matriz')
tridiag(n,d,a,c,b)


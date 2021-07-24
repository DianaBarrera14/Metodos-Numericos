# Definición de función
f1 = lambda x, y, z, w: (3 - y + z - 2*w)/7
f2 = lambda x, y, z, w: (-5 - x + 2*w)/8
f3 = lambda x, y, z, w: (4 + x + w)/4
f4 = lambda x, y, z, w: (-3 -2 * x + 2 * y+z)/6

# Inicializamos variables
x0 = 0
y0 = 0
z0 = 0
w0 = 0
cont = 0

#error tolerable
e = float(input('Ingrese el error tolerable: '))

# Implementación del método de iteración Jacobi
print('\nCont\tx\ty\tz\tw\n')

condition = True

while condition:
    x1 = f1(x0, y0, z0, w0)
    y1 = f2(x0, y0, z0, w0)
    z1 = f3(x0, y0, z0, w0)
    w1 = f4(x0, y0, z0, w0)

    print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' % (cont, x1, y1, z1,w1))
    e1 = abs(x0 - x1);
    e2 = abs(y0 - y1);
    e3 = abs(z0 - z1);
    e4 = abs(w0 - w1);

    cont += 1
    x0 = x1
    y0 = y1
    z0 = z1
    w0 = w1

    condition = e1 > e and e2 > e and e3 > e and e4 > e

print('\nSoluciones: x=%0.3f, y=%0.3f, z = %0.3f and w = %0.3f \n' % (x1, y1, z1,w1))


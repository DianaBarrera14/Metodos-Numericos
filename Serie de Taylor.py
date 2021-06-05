# 6. Diseñe un código que encuentre el sen(Π/3) a través del desarrollo de Taylor, trucar cuando n = 50

#DIANA FABIOLA BARRERA GALLO

#Importamos la librería para utilizar funciones matemáticas
import math

#Ingresamos por teclado el valor, en este caso 60
x_deg= float(input("Ingrese el numero del argumento en grados"))

#Funcion para transformar de radianes a grados
x=math.radians(x_deg)

#Ingresamos por el teclado valor de 50, ya que el programa nos pide
# truncar hasta cuando n=50
n=int(input("Introduzca el numero de terminos que desea sumar"))

#Inicializo acumulador en 0
sen_x = 0.0

#Acumulador de terminos
for c in range(n):

#Serie de Taylor
    sen_x = sen_x + (-1)**c * x**(2*c+1)/math.factorial((2*c+1))
    print(c,sen_x)






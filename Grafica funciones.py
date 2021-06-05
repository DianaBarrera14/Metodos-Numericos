# 3. Grafique en Python las siguientes funciones f(x) = x^2-x+1 y g(x)=\frac{2}{x-1}\
# Grafique ambas funciones en el mismo gráfico.

# DIANA FABIOLA BARRERA GALLO

#Importamos las librerías para utilizar funciones
# matemáticas y para realizar las gráficas
import numpy as np
import matplotlib.pyplot as plt

#Inicializo variables para la función cuadrática
a=1
b=-1
c=1

#Defino la función f(x) para que devuelva un valor
def f(x):
    return a*(x**2)+b*x+c

#Defino la función g(x) para que devuelva un valor
def g(x):
   return 2/(x - 1)

#Genero un vector espaciado linealmente
x = np.linspace(-15,15,1000)

#La función plot obtiene valores para los ejes x e y,
# y los muestra en un plano definido por la union de puntos.

plt.plot(x,f(x))
plt.plot(x,g(x))

#La función axvhline permite establecer el color de las
# abscisas y ordenadas en el plano cartesiano.

plt.axhline(0, color= "black")
plt.axvline(0, color= "black")

#La función xlim permite establecer el limite de las
#abscisas y ordenadas en el plano cartesiano.
plt.xlim(-20,20)
plt.ylim(-20,20)

#La función plt.show nos muestra la gráfica
plt.savefig("output.png")
plt.show()










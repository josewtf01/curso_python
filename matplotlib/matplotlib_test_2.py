import numpy as nupy
import matplotlib.pyplot as plt

# crear una figura de 8 x 6 puntos especificos (points),
# usando 100 puntos por pulgada (dpi)
plt.figure(figsize=(8,6), dpi=80)

# crear un subgráfica
plt.subplot(111)

# creamos un conjunto de datos de -PI a +PI
# entre esos dos tenemos 256 valores
X = nupy.linspace(-nupy.pi,nupy.pi,256,endpoint=True)

# creamos los valores de salida para las Funciones
# seno y coseno , con respecto a los valores de entrada
# de "X"

C, S = nupy.cos(X), nupy.sin(X)

# gráficamos la función coseno
# con los siguiente atributos

plt.plot(X, C, color="blue", linewidth=1.0, linestyle='-')

# gráficamos la función seno
# con los siguiente atributos

plt.plot(X, S, color="green", linewidth=1.0, linestyle='-')

# limitamos el eje "x"
plt.xlim(-4.0,4.0)

#limitamos el eje "y"
plt.ylim(-1.0,1.0)

# definimos una marca de referencia para el eje
# "x" tanto inicial como final
plt.xticks(nupy.linspace(-4,4,9,endpoint=True))

# definimos una marca de referencia para el eje
# "y" tanto inicial como final
plt.yticks(nupy.linspace(-1,1,5,endpoint=True))

# guardar gráfica con calidad de
# 80 pixeles por pulgada
plt.savefig("matplotlib_test_2.png",dpi=80)

# mostramos la gráfica creada
plt.show()

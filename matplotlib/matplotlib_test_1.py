# usar este comando si no está instalado matplotlib
# pip install matplotlib
# (anaconda):
# conda install -c conda-forge matplotlib
# conda install -c conda-forge/label/broken matplotlib
# conda install -c conda-forge/label/testing matplotlib
# conda install -c conda-forge/label/rc matplotlib

# está libreria fue creada para asimilar
# la graficación de matlab

# para utilizar funciones de gráficas en 2D
# utilizaremos el módulo pyplot

# numpy es muy utilizado al lado de matplotlib

# importamos el módulo pyplot de matplotlib
# como plt
import matplotlib.pyplot as plt

# importamos el módulo numpy de scipy como
# nupy
import numpy as nupy

# generamos nuestro conjuto de valores de entrada
# en este caso 256 valores entre -PI y +PI
X = nupy.linspace(-nupy.pi, nupy.pi, 256, endpoint=True)

# Imprimimos los diez primeros valores de nuestro
# conjunto de valores de entrada
print(X[0:10], "\n")

# Funciones trigonometricas coseno y seno
# creamos los valores de coseno y seno
# respecto a los valores de entrada de "X"
C, S = nupy.cos(X), nupy.sin(X)
# Imprimimos los primeros 10 valores de

#coseno
print( C[0:10] ,"\n")

#seno
print( S[0:10], "\n")

# gráficamos con la función plot de pyplot el

#coseno
plt.plot(X,C)

#seno
plt.plot(X,S)


# El eje "X" o de las ordenadas es siempre
# el primer argumento en la función plot()
# El eje "Y" o de las ordenadas es siempre
# el segundo argumento en la función plot()

# usamos la función show() de pyplot para
# mostrar las funciones trigonometricas
# en una sola gráfica
plt.show()

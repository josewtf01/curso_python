import numpy as nupy

# Podemos crear un arreglo de ceros en numpy
# con el siguiente atributo de los arreglos en numpy

# En este caso haremos una matriz de 3 x 4
matriz_ceros = nupy.zeros((3,4))
print("Impresión del arreglo: ")
print(matriz_ceros,"\n")
print("Tamaño de nuestro arreglo: ",matriz_ceros.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",matriz_ceros.ndim,"\n")
print("Tipo de de dato de cada dato: ",matriz_ceros.dtype.name,"\n")
print("Número de datos del arreglo: ",matriz_ceros.size,"\n")
print("Tamaño en bytes de cada dato: ",matriz_ceros.itemsize,"\n")

print("\n","----------Transición --------------\n")

# Tambien tenemos arreglos de unos
matriz_unos = nupy.ones((4,7))
print("Impresión del arreglo: ")
print(matriz_unos,"\n")
print("Tamaño de nuestro arreglo: ",matriz_unos.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",matriz_unos.ndim,"\n")
print("Tipo de de dato de cada dato: ",matriz_unos.dtype.name,"\n")
print("Número de datos del arreglo: ",matriz_unos.size,"\n")
print("Tamaño en bytes de cada dato: ",matriz_unos.itemsize,"\n")

print("\n","----------Transición--------------\n")

#por defecto si creamos un arreglo en numpy este tendra el tipo float64
# número de punto flotante de 64 bits

# para eso tenemos un atributo de los arreglos
estandar = nupy.empty((2,3))

print("Impresión del arreglo: ")
print(estandar,"\n")
print("Tamaño de nuestro arreglo: ",estandar.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",estandar.ndim,"\n")
print("Tipo de de dato de cada dato: ",estandar.dtype.name,"\n")
print("Número de datos del arreglo: ",estandar.size,"\n")
print("Tamaño en bytes de cada dato: ",estandar.itemsize,"\n")

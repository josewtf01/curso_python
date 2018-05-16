import numpy as nupy

# para crear arreglos de dimensiones mayores a 2
# tenemos varias formas
# la mas sencilla es hacer listas o tuplas anidadas

# en este caso haremos una matriz renglo de 1 x 2
# que cada elemento de esa matriz tenga a su vez
# una matriz cuadrada 2 * 2

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
mr_m =  nupy.array([a,b])

print("Impresión del arreglo: ")
print(mr_m,"\n")
print("Tamaño de nuestro arreglo: ",mr_m.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",mr_m.ndim,"\n")
print("Tipo de de dato de cada dato: ",mr_m.dtype.name,"\n")
print("Número de datos del arreglo: ",mr_m.size,"\n")
print("Tamaño en bytes de cada dato: ",mr_m.itemsize,"\n")
print("Tipo de clase: ",type(mr_m),"\n")

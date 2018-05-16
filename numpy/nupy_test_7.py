import numpy as nupy

a = nupy.arange(10000)
print("Impresión del arreglo: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",a.ndim,"\n")
print("Número de datos del arreglo: ",a.size,"\n")

print("\n","----------Transición mamalona--------------\n")

b = nupy.arange(10000).reshape((100,100))
print("Impresión del arreglo: ")
print(b,"\n")
print("Tamaño de nuestro arreglo: ",b.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",b.ndim,"\n")
print("Número de datos del arreglo: ",b.size,"\n")

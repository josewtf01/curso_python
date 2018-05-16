import numpy as nupy

a = nupy.array( [ [ 1 , 2 ] , [ 3 , 4 ] ] )

print("Impresión del arreglo: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",a.ndim,"\n")
print("Tipo de de dato de cada dato: ",a.dtype.name,"\n")
print("Número de datos del arreglo: ",a.size,"\n")
print("Tamaño en bytes de cada dato: ",a.itemsize,"\n")
print("Tipo de clase: ",type(a),"\n")

print("\n","----------Transición mamalona--------------\n")
# para hacer una matriz de flotantes tenemos un estilo de numpy
b = nupy.array([ [ 1. , 2. ] , [ 3. , 4. ] ])
print("Impresión del arreglo: ")
print(b,"\n")
print("Tamaño de nuestro arreglo: ",b.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",b.ndim,"\n")
print("Tipo de de dato de cada dato: ",b.dtype.name,"\n")
print("Número de datos del arreglo: ",b.size,"\n")
print("Tamaño en bytes de cada dato: ",b.itemsize,"\n")
print("Tipo de clase: ",type(b),"\n")

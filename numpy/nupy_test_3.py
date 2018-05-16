import numpy as nupy

# Nosotros podemos decirle al atributo array de numpy
# que tipo de dato queremos para nuestro arreglos
# este de manda como un argumento en el atributo array
c = nupy.array([ [ 1 , 2 ] , [ 3 , 4 ] ] , dtype=complex)

print("Impresión del arreglo: ")
print(c,"\n")
print("Tamaño de nuestro arreglo: ",c.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",c.ndim,"\n")
print("Tipo de de dato de cada dato: ",c.dtype.name,"\n")
print("Número de datos del arreglo: ",c.size,"\n")
print("Tamaño en bytes de cada dato: ",c.itemsize,"\n")
print("Tipo de clase: ",type(c),"\n")

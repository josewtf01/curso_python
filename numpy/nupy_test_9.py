import numpy as nupy

a = nupy.ones((2,3), dtype = int)
print("Impresión del arreglo a: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",a.ndim,"\n")
print("Tipo de de dato de cada dato: ",a.dtype.name,"\n")
print("Número de datos del arreglo: ",a.size,"\n")
print("Tamaño en bytes de cada dato: ",a.itemsize,"\n")

print("\n","----------Transición mamalona--------------\n")

b = nupy.random.random((2,3))
print("Impresión del arreglo b: ")
print(b,"\n")
print("Tamaño de nuestro arreglo: ",b.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",b.ndim,"\n")
print("Tipo de de dato de cada dato: ",b.dtype.name,"\n")
print("Número de datos del arreglo: ",b.size,"\n")
print("Tamaño en bytes de cada dato: ",b.itemsize,"\n")

print("\n","----------Transición mamalona--------------\n")

a *= 3
print("Impresión del arreglo a *= 3: ")
print(a,"\n")

a = (1/3)*a

print("\n","----------Transición mamalona--------------\n")
b += a
print("Impresión del arreglo b += a: ")
print(b,"\n")

b -= a

# versiones anteriores de numpy, marcaban error al tratar de convertir
# de tipos de datos de mayores bits a menores
# de acuerdo a eso de deja el siguiente bloque de código
try:
    a += b
    print("Impresión del arreglo a += b: ")
    print(a,"\n")
except e:
    print(e)

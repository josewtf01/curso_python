import numpy as nupy

a = nupy.random.random((2,3))
print("Impresión del arreglo a: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Número de datos del arreglo: ",a.size,"\n")
# tenemos varios atributos con operaciones utiles

print("\n","----------Transición mamalona--------------\n")

print("suma de todos los valores del arreglo: ")
print(a.sum(),"\n")

print("mínimo valor del arreglo: ")
print(a.min(),"\n")

print("máximo valor del arreglo: ")
print(a.max(),"\n")

print("\n","----------Transición mamalona--------------\n")

# tambien tenemos las denominadas funciones
# universales

c = nupy.arange(3)
print("Impresión del arreglo a: ")
print(c,"\n")
print("Tamaño de nuestro arreglo: ",c.shape,"\n")
print("Número de datos del arreglo: ",c.size,"\n")

print("exponencial del arreglo 'c' :")
print(nupy.exp(c),"\n")

print("raíz cuadrada del arreglo 'c' ")
print(nupy.sqrt(c),"\n")

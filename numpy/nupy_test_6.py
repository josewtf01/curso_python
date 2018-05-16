import numpy as nupy

# Para crear secuencias de números con arreglos, tenemos
# el siguiente atributo
a = nupy.arange(10,30,5)
# arange(inicio,final,pasos)
# si nosotros hacemos esto arange( n ) = arange( final )
# solo le mandaremos el final desde 0 hasta n-1
print("Impresión del arreglo: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",a.ndim,"\n")
print("Tipo de de dato de cada dato: ",a.dtype.name,"\n")
print("Número de datos del arreglo: ",a.size,"\n")
print("Tamaño en bytes de cada dato: ",a.itemsize,"\n")

print("\n","----------Transición mamalona--------------\n")

# podemos solo mandarle hasta que limite queremos
# nuestra secuencia de numeros
# ademas podemos agregar otro atributo
# para darle la forma que deseamos al arreglo
b = nupy.arange(12).reshape((3,4))
print("Impresión del arreglo: ")
print(b,"\n")
print("Tamaño de nuestro arreglo: ",b.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",b.ndim,"\n")
print("Tipo de de dato de cada dato: ",b.dtype.name,"\n")
print("Número de datos del arreglo: ",b.size,"\n")
print("Tamaño en bytes de cada dato: ",b.itemsize,"\n")

print("\n","----------Transición mamalona--------------\n")

# el atributo arange admite valores flotantes
c = nupy.arange(0 , 2 , 0.3)
print("Impresión del arreglo: ")
print(c,"\n")
print("Tamaño de nuestro arreglo: ",c.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",c.ndim,"\n")
print("Tipo de de dato de cada dato: ",c.dtype.name,"\n")
print("Número de datos del arreglo: ",c.size,"\n")
print("Tamaño en bytes de cada dato: ",c.itemsize,"\n")

print("\n","----------Transición mamalona--------------\n")

# una consideración al usar valores flotantes, es que
# no podemos saber cuantos datos estaran almacenados
# en nuestro arreglo , pudiendo incluo llegar a valores demasiado
# grandes

# para evitar eso tenemos un atributo
d = nupy.linspace(0,2,9)
# linspace(inicio, final , numero de datos*)
# * numero de datos entre el inicio y el final
print("Impresión del arreglo: ")
print(d,"\n")
print("Tamaño de nuestro arreglo: ",d.shape,"\n")
print("Numero de dimensiones o ejes del arreglo: ",d.ndim,"\n")
print("Tipo de de dato de cada dato: ",d.dtype.name,"\n")
print("Número de datos del arreglo: ",d.size,"\n")
print("Tamaño en bytes de cada dato: ",d.itemsize,"\n")

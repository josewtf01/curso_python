import numpy as nupy

a = nupy.arange(1,11)**2
print("Impresión del arreglo a: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Número de datos del arreglo: ",a.size,"\n")

# aquí tambien con arreglos en numpy
# se puede utilizar el rebanado
print("a[0] = ",a[0],"\n")
print("a[4] = ",a[4],"\n")
print("a[0:5] = ",a[0:5],"\n")
print("a[5:0] = ",a[5:0],"\n")
print("a[-10:-4] = ",a[-10:-4],"\n")
print("a[-4:-10] = ",a[-4:-10],"\n")

# tambien el arreglo de numpy es
# un objeto iterable con un for
print("for i in a: ")
for i in a:
    print(i)

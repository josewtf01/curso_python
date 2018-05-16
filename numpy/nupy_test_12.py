import numpy as nupy

a = nupy.arange(1,5).reshape((2,2))**2
print("Impresión del arreglo a: ")
print(a,"\n")
print("Tamaño de nuestro arreglo: ",a.shape,"\n")
print("Número de datos del arreglo: ",a.size,"\n")

# aquí tambien con arreglos en numpy
# se puede utilizar el rebanado
print("a[0] = ",a[0],"\n")
print("a[1] = ",a[1],"\n")
print("a[0][0] = ",a[0][0],"\n")
print("a[1][0] = ",a[1][0],"\n")
# tambien el arreglo de numpy es
# un objeto iterable con un for
print("for i in a: ")
for i in a:
    print(i)
print("\n")

print("for i in a for x in i :")
for row in a:
    for x in row:
        print(x)

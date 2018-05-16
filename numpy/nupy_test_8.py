import numpy as nupy

a = nupy.array([[1,1],[1,1]])
b = nupy.arange(1,5).reshape((2,2))
print("Impresión del arreglo a : ")
print(a,"\n")

print("Impresión del arreglo b : ")
print(b,"\n")

# operaciones basicas
c = a - b
print("Impresión del arreglo c  = a - b: ")
print(c,"\n")
# otra forma de hacer la resta es usando un atributo
# de los arreglos
# c = nupy.subtract(a,b)

c = a + b
print("Impresión del arreglo c  = a + b: ")
print(c,"\n")

# otra forma de hacer la suma es usando un atributo
# de los arreglos
# c = nupy.add(a,b)

# mulptiplicación elemento a elemento
c = a * b
print("Impresión del arreglo c  = a * b: ")
print(c,"\n")

# mulptiplicación matricial
c = a.dot(b)
print("Impresión del arreglo c  = a x b: ")
print(c,"\n")
# otra formal de hacer la mulptiplicación matricial
# c = nupy.dot(a,b)

c = b.dot(a)
print("Impresión del arreglo c  = b x a: ")
print(c,"\n")

c =  3 * a
print("Impresión del arreglo c  = 3 * a: ")
print(c,"\n")

# división elemento a elemento
c = a / b
print("Impresión del arreglo c  = a / b: ")
print(c,"\n")

# c = a / b -> c = a x b^(-1)
b_inv = nupy.linalg.inv(b)
c = a.dot(b_inv)
print("Impresión del arreglo c = a x b^(-1): ")
print(c,"\n")

c = (1/2) * b
print("Impresión del arreglo c  = (1/2) * b: ")
print(c,"\n")

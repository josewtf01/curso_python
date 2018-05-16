# eficiencia de python

# Podemos crear una lista 
# de la siguiente manera
squares = []
for x in range(10):
    squares.append(x**2)
print(squares,"\n")

# Otra forma (más eficiente) de crear
# la misma lista de arriba
squares = [x**2 for x in range(10)]
print(squares,"\n")

# Crear una lista de cuatro unos
one_list = [1]*4
print("lista -> ",one_list,"\n")

#crear una matriz en python
matriz = [[ x+(3*y) for x in range(1,4)] for y in range(3)]
print("matriz ->",matriz,"\n")

#Crear una tupla de de cuadrados
squares = [x**2 for x in range(10)]
squares = tuple(squares)
print("squares ->",squares,"\n")

# crear una tupla de cuatro ceros
tupla_1 = (0,)*4
print("tupla ->",tupla_1,"\n")

#crear un diccionario de cubos
# base (llave): base al cubo (valor)
cubes = {x:x**3 for x in range(10)}
print(cubes,"\n")

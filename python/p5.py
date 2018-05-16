# tuplas -> "tuple"

# Las tuplas en pocas palabras son lista, que no pueden 
# ser modificadas

# se declarán de la siguiente manera
tupla_1 = 123, "goku", -3.43
print("tupla -> ",tupla_1,"\n")
# Otra forma de declarar un tupla es 
tupla_1 = (123, "goku", -3.43)
print("tupla -> ",tupla_1,"\n\n\n")

# en las tuplas también podemos usar slicing para mostrar
# uno o varios datos
tupla_1 = ("goku", -3.1416, "luffy",17)
print("tupla -> ",tupla_1,"\n")
print("tupla[0] -> ",tupla_1[0],"\n")
print("tupla[1:4] -> ",tupla_1[1:4],"\n")
# una cosa a tomar en cuenta con el slicing o rebanada
# es que al usarlo este nos regresará una sub tupla de
# de la tupla original

#tupla de un solo dato
tupla_1 = 123,
print("tupla -> ",tupla_1,"\n")
# Otra forma de declarar un tupla es 
tupla_1 = (123,)
print("tupla -> ",tupla_1,"\n\n\n")
# una cosa a toamr en cuenta, necesitamos  # una coma despues de nuestro dato para 
# hacerlo tipo tupla,de lo 
# contrario tendrá el tipo de la variable
tupla_1 = (123)
print("tupla -> ",tupla_1,"\n")
print("tipo de dato -> ",type(tupla_1),"\n")
tupla_1 = (123,)
print("tupla -> ",tupla_1,"\n")
print("tipo de dato -> ",type(tupla_1),"\n")

#Podemos "sumar" dos tuplas, para hacer una
# de mayor tamaño de datos
tupla_1 = (1,2,3)
print("tupla_1 -> ",tupla_1,"\n")
tupla_2 = (4,5,6)
print("tupla_2 -> ",tupla_2,"\n")
tupla_total = tupla_1 + tupla_2
print("tupla_1 + tupla_2 ->",tupla_total,"\n")

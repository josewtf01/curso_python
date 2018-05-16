# listas

# una lista se declara de la siguiente forma
print("Estructura de dato : 'Lista' ")
lista_1 = [1, 2, 3, 4]
print("lista -> ", lista_1, "\n\n\n")

# Podemos tener una lista vacía 
print("Lista Vacía")
lista_1 = []
print("lista -> ", lista_1, "\n\n\n")

# Podemos saber la cantidad de elementos
# de una lista con una función por defecto
# del lenguaje
lista_1 = [1, 2, 3, 4]
num_dat = len(lista_1)

print("lista -> ", lista_1)
print("Número de datos de la lista ->", num_dat, "\n\n\n")

# La funcion len() -> lenght
# sirve para más estructuras de datos
# no solo lista
# por ejemplo:
# cadenas de texto
word = "python"
num_car = len(word)
print("word -> ", word)
print("Número de caracteres de la cadena de texto ->", num_car, "\n\n\n")

# Tenemos un atributo que nos permite
# agregar elementos al final de la lista
print("Lista Vacía")
lista_1 = []
print("lista -> ",lista_1, "\n")

#agregamos un dato con el atributo 
# append() de la lista
print("Agremamos un 3 a la lista")
lista_1.append(3)
print("lista -> ",lista_1,"\n")

#agregamos otro dato
print("Agremamos un 5 a la lista")
lista_1.append(5)
print("lista -> ",lista_1,"\n")

#agregamos otro dato más
print("Agremamos un 7 a la lista")
lista_1.append(7)
print("lista -> ", lista_1, "\n\n\n")

# lista_1.append( dato )
# esta atributo agrega datos al final de una lista

# Otra atributo para agregar datos en 
# una determinada posición
# es insert()
lista_1 = ["a", "c", "d"]
print("lista -> " ,lista_1, "\n")
print("""
[ "a", "c", "d"]
   0    1    2  """, "\n")
# agregamos "b" en la posición 1 de la lista 
# dicho de otra forma agregar "b" como el segundo elemento
# de la lista
lista_1.insert(1,"b")
print("Agregamos 'b' como segundo elemento de la lista" ,"\n")
print("lista -> ", lista_1, "\n")
print("""
[ "a", "b", "c", "d"]
   0    1    2    3  
   ""","\n\n\n")

# Una función del lenguaje para 
# listas y otras estructuras de datos 
# que nos permite borrar datos es del()

lista_1 = [10, 20, 30, 40]
print("lista -> ", lista_1, "\n")
#borramos el último dato
del(lista_1[3])
'''
Otra forma de borra el último dato

del(lista_1[len(lista_1)-1])

'''
print("lista -> ", lista_1, "\n\n\n")

# Tambien tenemos otro atributo 
lista_1 = ["jose", "maria", "natalia", "omar"]
print("lista -> ", lista_1, "\n")
# eliminamos jose de la lista
lista_1.remove("jose")
print("lista -> ", lista_1, "\n\n\n")
'''
Una cosa a recalcar aquí es que el atributo remove quita de la lista un data 
en especifico 
en este caso tenemos que indicarle que dato 
queremos remover de la lista
siendo esta, entero, flotante, cadena de texto, etc.
'''

# Una cosa a tomar en cuenta 
# si tenemos el mismo valor en la lista
# y usamos remove para eliminar ese dato
# lo que parasá es lo siguiente
lista_1 = ["apple", "dell", "toshiba", "dell", "lenovo"]
print("lista -> ", lista_1, "\n")
# quitamos dell de la lista con remove
lista_1.remove("dell")
print("lista -> ", lista_1, "\n\n\n")
'''
como podemos ver el atributo en caso de tener varios 
datos iguales elimina el primero que este en la lista
usando los indices, o sea
["apple", "dell", "toshiba","dell","lenovo"]
   0        1         2        3         4  
la cadena dell como elemento 1 de la lista
es el que será eliminado con la función remove
'''
# Por último tenemos el atributo pop() 
# para eliminar un dato
lista_1 = ["a", "b","c","d"]
print("lista -<",lista_1,"\n")
dato_remove = lista_1.remove("a")
print("lista -<",lista_1,"\n")
print("dato_remove : ",dato_remove,"\n")
lista_1 = ["a", "b","c","d"]
print("lista -<",lista_1,"\n")
dato_pop = lista_1.pop(0)
print("lista -<",lista_1,"\n")
print("dato_pop : ",dato_pop,"\n\n\n")
'''
la diferencia entre  
del(lista_1[0]) -> eliminar la "a"
lista.remove("a") -> eliminar la "a"
lista.pop(0)->eliminar la "a"

--lista_1 = ["a", "b", "c", "d"]

es que tanto remove y del() borran el dato de la lista, pero no lo regresan. Y pop() borra el dato de la lista, pero regresa el dato a borrar 

'''

# podemos tambien usar el slicing
#  o rebanado con las listas
squares = [1,4,9,16,25]
'''
[ 1, 4, 9, 16, 25]
  0  1  2   3   4
 -5 -4 -3  -2  -1
'''

print("lista -> ", squares, "\n")
print("los primeros dos datos de la lista -> ",squares[:2],"\n")
# squares[0:2] = squares[:2] = squares[:-3]
print("los últimos dos datos de la lista -> ",squares[-2:],"\n")
# squares[-2:] = squares[3:]

'''
Algo a tomar en cuenta es que 
los indices los cuales deben de ir 
0 -> 5  y de -5 a -1
Sí, se invierte esto
se nos regresará una lista vacía
'''
print("lista[-1:-5] ->", squares[-1:-5], "\n\n\n")

# Las lista son mutables
# es decir, que podemos cambiar un datoo varios datos
# de la lista
cubes = [1, 8, 26, 64]
print("lista -> ", cubes, "\n")
#tenemos mal el cubo de 3 que es 27
cubes[2] = 27
print("lista -> ", cubes, "\n\n\n")

lista_1 = ["Aple", "Del", "Toshba", "Lenovo", "Asus"]
print("lista -> ", lista_1, "\n")

# las tres primeras cadenas de texto de la 
# lista están mal escritas

lista_1[0:3] = "Apple", "Dell", "Toshiba"
# otra forma de hacerlo
'''
lista_1[0], lista_1[1], lista_1[2] = "Apple", "Dell",   "Toshiba"
'''
print("lista -> ", lista_1, "\n\n\n")

# podemos acomodar los datos de una lista
# con el atributo sort
lista_1 = [3,4,2,1,-7,-3,0]
print("lista desordenada -> ",lista_1,"\n")
lista_1.sort()
print("lista ordenada -> ",lista_1,"\n\n\n")

# Podemos ordenar una lista de cadenas de texto, con sort
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("lista desordenada -> ",fruits,"\n")
fruits.sort()
print("lista ordenada -> ",fruits,"\n\n\n")
# La ordenación con cadenas de texto, se basa en el 
# formato ASCII
# por lo tanto primero se pondrán mayúsculas
# y despues minúsculas
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana',"Apple"]
print("lista desordenada -> ",fruits,"\n")
fruits.sort()
print("lista ordenada -> ",fruits,"\n\n\n")

#otra atributo es index()
# que nos da el indice del primer dato que encuentre
# en la lista
lista_1 = [1,2,3,1,5,6]
print("lista -> ",lista_1,"\n")
print("indice de 1 en la lista ->",lista_1.index(1),"\n")
# Para que nos de el indice del segundo 1 después de 
# 3 tenemos que indicar en que rango queremos que busque 
# la función 
lista_1 = [1,2,3,1,5,6]
print("lista -> ",lista_1,"\n")
print("indice de 1 en la lista ->",lista_1.index(1,2,5),"\n\n\n")
# aquí le dijimos que buscará entre la posición 2 a la posición 5 de la lista

# Tenemos otro atributo que 
# cuenta cuantas veces tenemos
# un dato especifico en nuestra lista
# es count()
lista_1 = [1,3,1,5,7,6,5,8,1]
print("lista -> ",lista_1,"\n")
print("1 en la lista ->",lista_1.count(1),"veces\n")
print("5 en la lista ->",lista_1.count(5),"veces\n\n\n")

# Otro atributo más es reverse()
# la cual cambiar el orden en 
# reversa de los datos en la lista
lista_1 = ["a","b","c","d"]
print("lista original -> ",lista_1,"\n")
lista_1.reverse()
print("lista en reversa -> ",lista_1,"\n\n\n")

# podemos "juntar"lista para hacer una sola
lista_1 = [1,2]
lista_2 = [3,4]
lista_3 = lista_1 + lista_2
print("lista_1 -> ",lista_1,"\n")
print("lista_2 -> ",lista_2,"\n")
print("lista_3  = lista_1 + lista_2 -> ",lista_3,"\n\n\n")

# otra forma de juntar listas
  lista_1 = ["a", "b"]
  print("lista_1 -> ",lista_1,"\n")
  lista_1 = lista_1 + ["c","d"]
  print("lista_1 = lista_1 + ['c','d'] -> ",lista_1,"\n\n\n")

# podemos tener listas anidadas
# por ejemplo una matrix de 2x2
# hecha con listas
lista_1 = ["a","b"]
print("lista_1 -> ",lista_1,"\n")
lista_2 = ["c","d"]
print("lista_2 -> ",lista_2,"\n")
matriz = [lista_1,lista_2]
print("matriz -> ",matriz,"\n")

# primer elemento de la matriz es la lista 
# ["a", "b"]
print("matriz[0] -> ",matriz[0],"\n")

# primer elemento de la primera lista
# "a"
print("matriz[0][0] -> ",matriz[0][0],"\n")

# y así para los demas elementos
print("matriz[0][1] -> ",matriz[0][1],"\n")
print("matriz[1] -> ",matriz[1],"\n")

print("matriz[1][0] -> ",matriz[1][0],"\n")
print("matriz[1][1] -> ",matriz[1][1],"\n")

'''
algunos atributos para listas son:

list.append(dato)

list.insert(indice,dato)

list.pop() / list.pop(indice)

list.index(dato) /list.index[dato,inicio,final]

list.count(dato)

list.sort()

list.reverse()

'''
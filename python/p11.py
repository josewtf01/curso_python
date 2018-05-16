# sentencias for 
'''
Las senticias for son ciclos de control
que nos permiten ejecutar algoritmos 
un determinado número de veces.
El número de veces que se ejecutará es conocido por el programador.
Las setencias for son algo abstractas 
a diferencia de otros lenguajes
'''
# Ejemplo
words = ["cat", "spider", "dog"]
for x in words:
    print(x,end = ", ")
    print("cantidad de letras:",end = " ") 
    print(len(x),"\n")
'''
en este ejemplo declaramos un variable
"x" la cual tomara el valor del elemento 
de la lista por cada iteración.
la setencia for acabará , cuando ya no haya elementos que evaluar en la lista
'''

"""
Si queremos que nuestra setencia for 
se ejecute un determinado número de veces
usamos la función 
range(inicio,final,incremento).

La función range es exclusiva, es decir,
tomarará en cuenta al inicio , pero no tomará en cuenta el final.

Ejemplo: 
range(1,10,1) -> 1,2,3,4,5,6,7,8,9
da los mismo no poner el incremento si este
es igual a 1.

range(1,10,1) = range(1,10) 
range(1,10)-> 1,2,3,4,5,6,7,8,9
"""
# Ejemplo range(1,10,1) = range(1,10)
for x in range(1,10,1):
    print(x,end = ", ")

print("\n")

for x in range(1,10):
    print(x,end = ", ")
print("\n")

# Siguiente ejemplo 
for x in range(10,100,10):
    print(x,end = ", ")

print("\n")

for x in range(-1,-10,-1):
    print(x, end = ", ")
print("\n")

# si nosotros invertimos de mayor a menor
#  en este caso -10 a -1
# el for no se ejecutará
for x in range(-10,-1,-1):
    print(x, end = ", ")
print("\n")
"""
Tambien podemos dejar 
range(10) -> 0,1,2,3,4,5,6,7,8,9
esto solo tomará el 10 como valor final
y dejara por defecto al 0 como inicio
"""
for x in range(10):
    print(x, end = ", ")
print("\n")

# El siguiente bloque de código 
# no se ejecutará
for x in range(-10):
    print(x, end = ", ")
print("\n")

# Ejemplo con función len() -> cantidad 
# de datos en lista
animals = ["dog","cat","spider","gecko"]
print("animals -> ", animals,"\n")
for x in range(len(animals)):
    print("pocisión : ",x, end = " ")
    print("-> ",animals[x])
print("\n")
# tenemos dos funciones del lenguaje
# que aplican para listas

# La función break
# termina un ciclo de control abruptamente
# antes de terminar el ciclo de control
for x in range(10):
    if x >5:
        break
    print(x,end = ", ")
print("\n\n")

# La función continue
# salta una iteración del ciclo de control
# abruptamente permitiendo continuar
# el ciclo de control

for x in range(10):
    if x % 2 ==0:
        continue
    print(x,end = ", ")
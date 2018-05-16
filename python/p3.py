'''
Slicing o rebanado
Aplicado a cadenas de texto
'''

'''
De izquieda a derecha iniciamos 
contando desde 0 hasta n-1 carácteres 
que tenga la cadena de texto
'''
#   p  y  t  h  o  n
#   0  1  2  3  4  5

"""
De derecha a izquierda contamos desde -1
hasta -(n) carácteres de longitud que
tenga la cadena de texto
"""
#   p  y  t  h  o  n
#  -6 -5 -4 -3 -2 -1


# Utilizaremos la palabra python como
# ejemplo

#   p  y  t  h  o  n
#   0  1  2  3  4  5  izq -> der
#  -6 -5 -4 -3 -2 -1  der -> izq

word = 'python'
print(" \nword -> ", word, "\n")
print(
'''
   p  y  t  h  o  n
   0  1  2  3  4  5
  -6 -5 -4 -3 -2 -1
''', "\n")

# Queremos el primer caracter

# izquierda a derecha
print("word[0] -> ", word[0], "\n")

# de derecha a izquierda sería
print("word[-6] -> ", word[-6], "\n")

# Queremos el último caracter

# izquierda a derecha
print("word[5] -> ", word[5], "\n")

# de derecha a izquierda sería
print("word[-1] -> ", word[-1], "\n")

'''
El rebanado nos permite no solo 
tomar un caracter. Nos permite 
tomar de uno a varios caracteres
para hacer esto usamos la siguiente
propiedad del lenguaje
'''

# word[inicio : final ]

# Sí nosotros no indicamos nada antes 
# y despues de los dos puntos, el interprete
# mostrará la cadena completa
print("word[:] -> ",word[:], "\n")

# los primeros tres caracteres
print("word[0:3] -> ", word[0:3], "\n")
print("word[-6:-3] -> ",word[-6:-3],"\n")

#otra forma sería solo indicar el final
print("word[:3] -> ", word[:3], "\n")
print("word[:-3] -> ",word[:-3],"\n")


# Los últimos tres carácteres
print("word[3:6] -> ",word[3:6],"\n")
print("word[3:] -> ", word[3:], "\n")

"""
nota: si ponemos esto en nuestro 
código
print(word[-3:-1])
imprimira desde el tercer caracter hasta el
penultimo
en este ejemplo
word = "python"
word[-3:-1] -> "ho"
para evitar esto entonces solo indicamos 
el inicio del caracter 
"""
# para evitar que no falta el último
# carácter
print("word[-3:] -> ", word[-3:], "\n")

'''
Con estos dos ejemplos podemos
darnos cuenta que el slicing es
una herramienta poderosa del 
lenguaje. Algo tomar en cuenta del
slicing es que es exclusivo, es decir,
toma en cuenta desde el primer valor
pero excluye el limite del final
por ejemplo:

word[0:3] = "pyt" no "pyth"
donde h sería el 3 caracter

otro ejemplo sería 
word[0:5] -> "pytho" y no "python"
'''

# otra cosa a recalcar 
# sería este detalle
print("word[6:0] -> ", word[6:0], "\n")
print("word[-1:-6] -> ", word[-1:-6], "\n")

'''
Como pude apreciar estas dos salidas 
no imprime ninguna carácter
por lo tanto el slicing debe realizarse de
la siguiente manera:

para indeces positivos
-> 0 (inicio) -> n-1 (final) 

para indices negativos
-> -n(inicio) -> -1 (final)

'''

"""
Otra cosa a mencionar, podemos combinar
indices negativos y positivos
"""
#   p  y  t  h  o  n
#   0  1  2  3  4  5  izq -> der
#  -6 -5 -4 -3 -2 -1  der -> izq

# contando desde el segundo caracter
# excluyendo el último caracter
print("word[1:-1] -> ", word[1:-1], "\n")

#contando desde el tercer caracter y
# excluyendo los últimos dos
print("word[2:-2] -> ", word[2:-2], "\n")

# Otra cosa importante a recalcar
# es que las cadenas de texto son 
# inmutables, es decir, no pudes alterar
# uno o varios caracteres

# word[0] = "C" , esto marcará error
# word[0:3] = "nis" esto marcará error

# solo podemos cambiar la cadena
# completamente
word = "cython"
print("word -> ", word, "\n")

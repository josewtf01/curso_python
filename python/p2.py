# Cadenas 

# Declarar var_1  = "python"
var_1 = "python"
print(var_1, "\n")

# Declarar var_1 = 'python'
var_1 = 'python'
print(var_1, "\n")

# La diferencia entre comillas dobles
# " " y comillas simples ' '
# para las cadenas de texto es la 
# ambigüedad que puedan causar estás
# con el idioma o caracteres especiales

# Ejemplo de comillas
s_1 = "I'm a super coder"
s_2 = 'He is the "coder" '
print(s_1, "\n")
print(s_2, "\n")

# otro detalle con las cadenas de texto
# es cuando queremos imprimir cadenas con
# caracteres que el interprete toma en 
# sentido del lenguaje

# Ejemplo de caracter especial
# esto mostrará \n como salto de linea
# no como la dirección de una carpeta
s_1 = "C:\some\name"
print(s_1, "\n")
'''
Lo imprimirá como : 

C:\some
ame

'''


# para evitar eso utilizamos
# cadenas "crudas" => raw (inglés)
s_1 = r"C:\some\name"
print(s_1, '\n')

# Podemos tener cadenas de texto
# multilineas
s_1 = '''Esto es una prueba 
multilinea para
ejemplos didacticos'''
print(s_1, "\n")
# no hay diferencia aquí en cadenas 
# multilineas, pero hay que tener cuidado
# con las comillas simples o dobles 
# como se mostro en ejemplos arriba 
# de este archivo
s_2 = """Otro ejemplo
didactico
para cadenas
"""
print(s_2,"\n")

# Tenemos las concatenación de cadenas
# tipo suma 
print("Alicia" + " y " + "Bob", "\n")
#otra forma de ponerlo
s_1 = "Alicia"
s_2 = " y "
s_3 = "Bob"
print(s_1 + s_2 + s_3, "\n")

# Podemos hacer una cadena
# de una cadena de texto 
# un número determinado de veces

# En este ejemplo tenemos 
# que se imprimirá la cadena
# tres veces y la mostrará concatenada
print("ABC_" * 3)

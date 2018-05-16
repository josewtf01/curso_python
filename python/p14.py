# formatos en python para salida
# de datos
cadena_texto = "I'm Jose"

print(str(cadena_texto))
print(repr(cadena_texto))
print("\n")
cadena_texto = "Hello, World.\n python"

print(str(cadena_texto))
print(repr(cadena_texto))
print("\n")

# ejemplo de cadena de texto con atributo
# format
a, b, c = 'uno', 2, 3.1415926535

print("%s , %i , %.2f" %(a,b,c))
print('{z}, {y}, {x}'.format(x=a,y=b,z=c))

print("{}, {}, {}")

# Las cadenas de texto en python
# son también tomadas como un objeto
# * ver referencia en programación
# orientada a objetos para más detalle


print("\n")
# formato para salida de una tabla
for x in range(1, 11):
    print(repr(x).rjust(2), end=' ')
    print(repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
print("\n")


# Otra forma para dar formato
# a nuestra tabla
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print("\n")


# atributo format para cadenas
s ="c:\some\name"
#cadena cruda !r
print("cadena -> {!r}".format(s))
# cadena formato ascii !a
print("cadena -> {!a}".format(s))
# cadena tomada por el interprete !s
print("cadena -> {!s}".format(s))
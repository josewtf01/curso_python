# sentencias if, elif (else if) y else

# Tenemos un forma de hacer que nuestros
# programas tomen deciciones y esta es
# através de las sentencias if , elif y else

# Nota aprobatoria
# escala de 0.0 a 10.0
nota = input("La nota de la materia es: \n")
nota = float(nota)
if nota < 7.0:
    print("Has reprobado la materia\n")
else:
    print("Has aprobado la materia\n")

# evitar que el valor ingresado no sea
#un número
'''
try:
    val = float(nota)
    if val < 7.0:
        print("Has reprobado la materia\n")
    else:
        print("Has aprobado la materia\n")
except ValueError:
    print("el valor ingresado no es un número")
'''

# Ejemplo con sentencia elif

numero = input("Ingresa un numéro \n entre -10.0 a 10.0 \n ")
numero = float(numero)
if numero < 0.0:
    print("número negativo \n")
elif numero == 0:
    print("cero \n")
else:
    print("Número positivo \n")

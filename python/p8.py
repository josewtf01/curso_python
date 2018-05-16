# Tenemos una nueva función 
# del lenguaje 

nombre = input("dame tu nombre : ")
print("Bienvenido " + nombre, "\n")

# Esta función "input"toma un valor que sea 
# ingresado por el usuario
edad = input("¿Cuál es tu edad? ")
print("Tienes " , edad , " años \n" )

'''
Una desventaja de está función 
es cuando se trata de ingresar números
nosotros al ingresar un número la
función "input" lo tomará como cadena
de texto
'''
height = input("¿Cuál es tu estatura? ")
print(height + "\n")
# Para evitar esto tenemos que convertir
# la cadena de texto al tipo de variable 
# deseado, esto se conoce como "casting"
height = float(height)
print("te faltan ", round(2.0-height,2),"m para los dos metros \n")

# Nota , se uso la función 
# round(number,decimal_digits) para 
# redondear el resultado decimal de la 
# operación

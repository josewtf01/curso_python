# diccionarios  ->"dictionaries"

# los diccionarios son una estructura de
# datos las cuales tiene pares de datos
# key:value , donde la key o llave es el 
# identificador y value o valor, el dato 
# que se le asocia a la llave

#se declarán de la siguiente manera
telefonos = {"jose":111,"maria":112,"pedro":113}
print("diccionario -> ",telefonos,"\n\n\n")
# declaramos un diccionario como un agenda
# de telefonos, aquí las llaves o keys son 
# los nombres de las personas y 
# los valores , los números telefonicos

# si queremos solo las llaves de un
# diccionario usamos el atributo keys
canciones = {1:"wake me up",2:"basket case"}
print("diccionario -> ",canciones,"\n")
llaves = canciones.keys()
print("keys -> ",llaves,"\n")
# si solo queremos los valores del 
# diccionario usamos el atributo values
print("values -> ",canciones.values(),"\n\n\n")

# podemos agregar un dato al diccionario 
# usando la siguiente sintaxis 
num_eng = {1:"one",2:"two"}
print("diccionario -> ",num_eng,"\n")
num_eng[3] = "three"
print("diccionario -> ",num_eng,"\n\n\n")

# con la misma sintaxis para agregar datos
# nosotros podemos obtener datos
tools = {1:"pico",2:"pala",3:"martillo"}
print("diccionario -> ",tools,"\n")
print("tools[1] ->",tools[1],"\n")
print("tools[2] ->",tools[2],"\n")
print("tools[3] ->",tools[3],"\n")

# Si queremos conocer todos los elementos 
# de un diccionario
# usamos la el atributo items()
dic = {1:"day",2:"night",3:"evening"}
print("items -> ",dic.items(),"\n")

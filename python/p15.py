# lectura y escritura de archivos

#escritura
f = open("workfile_1.txt","w")
# w -> write, r -> read
# a -> append, b -> binary
# r+ -> write and read
# si no especificamos el modo del archivo
# este por defecto tomará en escritura
f.write("Line 1\n")
f.write("Line 2\n")
f.write("Line 3\n")
f.write("Line 4\n")
f.close()

# lectura 
f = open("workfile_1.txt","r")
# print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
# print(f.readline())
f.close()

# escritura en utf-8
# su editor de texto debe manejar
# esta codificación para ver los datos
# tales como los mandamos como codigo
import codecs
file = codecs.open('workfile_2.txt','w','utf-8')
file.write("Línea 1 \n")
file.write("Línea 2 \n")
file.write("Línea 3 \n")
file.write("Línea 4 \n")

file.close()

# tenemos otra forma de ejecutar archivos
# de texto sin tener que preocuparnos
# por cerrar el archivo y tener problemas 
# el buffer de salida para el teclado
with open("workfile_3.txt","w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")
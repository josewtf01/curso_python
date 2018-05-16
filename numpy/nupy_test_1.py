import numpy as nupy

# usar este comando si no tiene instalado numpy
# pip install numpy ó pip install scipy
# easy_isntall numpy ó easy_install scipy
# (anaconda): conda install -c anaconda scipy


# numpy tiene un atributo el cual nos permite crear arreglos de varias dimensiones
# un arreglo en numpy tiene el mismo tipo de dato, esto por cuestiones de operaciones
# y cuestiones de eficiencia en operaciones

# aquí creamos un arreglo de una sola dimension
# podemos referirlo como una matriz renglon en este caso
a = nupy.array([1,2,3,4])

# Podemos tanto mandarle una lista y/o listas anidadas
# o en su caso tuplas y/o tuplas anidadas
# a = nupy.array((1,2,3,4))

#impresión de nuestra matriz renglon
print("Impresión del arreglo: ")
print(a,"\n")

# Tenemos un atributo de los arreglos el cual nos dice sus dimensiones
# En numpy las dimensiones se le conocen como "ejes"
print("Tamaño de nuestro arreglo: ",a.shape,"\n")

# Tenemos un atributo de los arreglos el cual nos dice el número de dimensiones
# en numpy al número de dimensiones se le conoce como "rango"
print("Numero de dimensiones o ejes del arreglo: ",a.ndim,"\n")

# Tenemos otro atributo que nos dice el tipo de los datos de nuestro arreglo
print("Tipo de dato de cada dato: ",a.dtype.name,"\n")
# Otra manera de obtener el tipo de los datos de nuestro arreglo
# print("Tipo de dato de cada dato: ",a.dtype,"\n")

# Tenemos otro atributo el cual nos dice la cantidad de datos totales en el arreglo
print("Número de datos del arreglo: ",a.size,"\n")
# Tenemos otro atributo el cual nos dice el tamaño en bytes de cada datos
# el cual es el mismo para cada dato al ser todos el mismo tipo
print("Tamaño en bytes de cada dato: ",a.itemsize,"\n")

# Imprimimos que tipo de objeto es el arreglo de numpy
print("Tipo de clase: ",type(a),"\n")

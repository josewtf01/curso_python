# conjuntos -> "sets"

# un conjunto es una serie de datos,
# pero un conjunto solo puede tener un dato
# en especifico solo una vez en este

# Como ejemplo
basket = {"apple","orange","apple","pear","apple","orange","Apple"}
print("conjunto -> ",basket,"\n")
# como podemos ver aunque haya dentro del 
# conjunto dos o más valores iguales
# el conjunto solo tendrá una vez el dato

# podemos crear un conjunto con la
# la función set()
conjunto = set("murcielago")
print("conjunto -> ",conjunto,"\n")

# tenemos varias operaciones con conjuntos
# que se ven en diagramas de venn en 
# matemáticas
a = set("pokemon")
b = set("digimon")
print("conjunto a -> ",a,"\n")
print("conjunto b -> ",b,"\n")

# Diferencia -> a-b
print("direfencia [a,b]>",a-b,"\n")

# Unión -> a | b
print("unión [a,b] -> ",a|b,"\n")

# Intersección -> a & b
print("Intersección [a,b] ->",a&b,"\n")

# diferencia simetrica -> a^b
print("Diff. Simetrica [a,b] -> ",a^b,"\n\n\n")

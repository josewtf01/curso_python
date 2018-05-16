# primer paso I

# importamos el conjuto de datos
# estos seran nuestros datos de entrenamiento
from sklearn.datasets import load_iris

# los datos de entrenamiento los
# asignamos a una variable
iris = load_iris()

# imprimimos las características de los datos
print(iris.feature_names,"\n")

# imprimimos las etiquetas de los tados
print(iris.target_names,"\n")

# imprimimos el primer ejemplo
# ó primer renglón de nuestro conjunto
# de datos

#print(iris.data[0],"\n")
#print(iris.data[0][0],"\n")
#print(iris.target[0],"\n")


# imprimimos todos los ejemplos con sus
# características y etiquetas
for i in range(len(iris.target)):
    print("Example %d:" %(i) ,end='')
    print(" Label %s" %(iris.target[i]),end='')
    print(" Features %s" %(iris.data[i]), end='')
    print("\n")


# referencias
# http://scikit-learn.org/stable/datasets/index.html
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# https://es.wikipedia.org/wiki/Iris_flor_conjunto_de_datos

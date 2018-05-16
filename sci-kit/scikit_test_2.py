# Paso dos I
# cargamos los datos de entrenamiento

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

#cargamos los datos , en este caso
# los datos de la flor iris
# la cual son tres variantes de la flor
iris = load_iris()

# para este ejemplo se eliminaran
# tres ejemplos de nuestro conjunto
# de datos de entrenamiento
# y luego se volveran a predecir

# elegimos eliminar el primer
# ejemplo de iris setosa
# primer ejemplo de iris versicolor
# primer ejemplo virginica
# eliminando 3 ejemplos de nuestros
# 150 ejemplos
test_idx = [0,50,100]

# creamos los datos de entrenamiento
# eliminando tres ejemplos

# eliminamos primero las etiquetas
train_target = np.delete(iris.target, test_idx)
# luego eliminamos sus características
train_data = np.delete(iris.data, test_idx, axis = 0)

# usamos datos de prueba
# los cuales son los tres ejemplos
# que eliminamos
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# paso dos II 
# se crea el clasificador
classifier = tree.DecisionTreeClassifier()

# se entrena el clasificador
classifier = classifier.fit(train_data,train_target)

# paso tres III
# predecir algunos ejemplos
# en este caso prediciremos los datos eliminados

# primero imprimimos las etiquetas de los ejemplos
# "reales" por asi decirlo
print(test_target,"\n")

# imprimimos nuestras predicciones
print(classifier.predict(test_data))

# Paso IV
# visualizar el árbol de decisiones

# instalar librería graphviz

# vía pip
# pip install graphviz

# vía anaconda
# conda install -c conda-forge python-graphviz

# instalar librería IPython

# vía pip
# pip install ipython

# vía anaconda
# conda install -c anaconda ipython

# instalar vía anaconda conforme a la documentación
# conda install python-graphviz

# para más información
# http://scikit-learn.org/stable/modules/tree.html#tree
# http://graphviz.readthedocs.io/en/stable/manual.html

import graphviz
dot_data = tree.export_graphviz(classifier, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")

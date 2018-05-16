# vía de instalación

# vía pip
# pip install scikit-learn
# ó pip install -U scikit-learn

# vía anaconda
# conda install -c anaconda scikit-learn

# importamos la libreria de scikit-learn
import sklearn
from sklearn import tree

# se le llama datos de entrenamiento
# al conjunto de características y etiquetas

# tenemos las carácteristicas aquellas que podemos
# medir o cuantizar

#features = [[140,"smooth"],[130,"smooth"],[150,"bumpy"],[170,"bumpy"]]
features = [[140,1],[130,1],[150,0],[170,0]]

# las etiquetas son el individuo o objeto como
# tal al cual le podemos asignara varias
# características medibles o cuantizadas

labels = ["apple","apple","orange","orange"]
#labels = [0,0,1,1]

# con la libreria definimos el tipo de
# clasificador
# en este caso un árbol de decisiones

classifier = tree.DecisionTreeClassifier()

# aquí hacemos que la librería haga
# el entrenamiento con los datos de entrenamiento
classifier = classifier.fit(features,labels)

# después de entrenar el clasificador
# pasamos a hacer prediciones
# que tan buena sea o no nuestra
# predicción dependera de gran medida
# del numéro de ejemplos para entrenar
# nuestro clasificador

print(classifier.predict([[160,0]]))

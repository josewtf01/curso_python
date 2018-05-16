# para instalar opencv con pip
# pip install opencv-python

# para instalar opencv con anaconda
# conda install -c conda-forge opencv
# ó    conda install -c conda-forge/label/broken opencv

#importamos la libreria de opencv
import cv2

#creamos una variable que lea los datos de nuestra imagen
imagen = cv2.imread("colores.jpg")

# mostramos la imagen a través de una función de opencv
# mandando el titulo de la ventana, y la variable con los datos
# de la imagen
cv2.imshow("Colores",imagen)

#esperamos a que pulsemos una tecla para quitar la ventana
cv2.waitKey(0)

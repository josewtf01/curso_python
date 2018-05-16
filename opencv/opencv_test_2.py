import cv2

imagen_1 = cv2.imread("colores.jpg")

imagen_2 = cv2.imread("colores.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("imagen a colores",imagen_1)
cv2.waitKey(0)
cv2.imshow("imagen a escala de grises",imagen_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

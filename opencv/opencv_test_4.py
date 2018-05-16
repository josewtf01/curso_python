import cv2
import matplotlib.pyplot as plt

imagen_1 = cv2.imread("colores.jpg")
cv2.imshow("imagen a colores",imagen_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(imagen_1)
plt.xticks([]),plt.yticks([])
plt.show()
plt.close()

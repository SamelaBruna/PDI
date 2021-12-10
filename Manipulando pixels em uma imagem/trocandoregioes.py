import cv2 as cv
import numpy as np

img = cv.imread("../Fotos/biel.png")
sizeImg = np.shape(img)
height = sizeImg[0]
width = sizeImg[1]

#Criando 4 imagens a partir da original
img1 = img[0:height//2, 0:width//2]
img2 = img[0:height//2, width//2:width]
img3 = img[height//2:height, 0:width//2]
img4 = img[height//2:height,width//2:width]
print(img1.shape)

#criando uma imagem nova a partir da função zeros com mesma altura e largura da original
newImg = np.zeros((height,width,3), np.uint8)

#alocando as imagens criadas em uma nova imagem
newImg[0:height//2, 0:width//2] = img4
newImg[0:height//2, width//2:width] = img3
newImg[height//2:height, 0:width//2] = img2
newImg[height//2:height,width//2:width] = img1

#mostrando e salvando as imagens
cv.imshow("Antes",img)
cv.imwrite("../Fotos/Antes.jpg", img)
cv.imshow("Depois",newImg)
cv.imwrite("../Fotos/Depois.jpg", newImg)
cv.waitKey(0)
cv.destroyAllWindows()

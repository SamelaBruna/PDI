import cv2 as cv
import numpy as np
import random


img = cv.imread("../Fotos/levi.jpg",cv.IMREAD_GRAYSCALE)
cv.imshow("inicial",img)
sizeImg = np.shape(img)
height = sizeImg[0]
width = sizeImg[1]

#Função para adicionar pontos aleatoriamente na imagem
def points(img1):
    radius = 3
    imgPont = img.copy()
    for i in range(0,height,radius):
        for j in range(0,width,radius):
            number = random.randint(0,1)
            if number == 0:
                continue
            gray = int(img[i][j])
            color = (gray, gray, gray)
            cv.circle(imgPont, (j, i), radius, color, radius)
            radius = random.randint(1, 4)

    return imgPont

#Aplicando o filtro de Canny
edgesImg = cv.Canny(img,100,200)
imgPon = points(img)
sizeImgPont = np.shape(img)
heightPont = sizeImgPont[0]
widthPont = sizeImgPont[1]

radius = 3

# Após aplicar o filtro de canny onde houver pixels com valor de 255 desenhará circulos
for i in range(heightPont):
    for j in range(widthPont):
        if (edgesImg[i][j] == 255):
            gray = int(img[i][j])
            color = (gray, gray, gray)
            cv.circle(imgPon, (j, i), radius, color, radius)


cv.imshow("Imagem Final",imgPon)
cv.imwrite("../Fotos/ImgFinal.jpg", imgPon)
cv.waitKey(0)
cv.destroyAllWindows()




import cv2 as cv
import numpy as np

img = cv.imread("../Fotos/biel.png")
#tamanho da imagem
sizeImg = np.shape(img)
print(sizeImg)

#Para negativar uma imagem é necessário subtrair 255 do seu valor no pixel
def spaceNegative(P1,P2,img):

    for i in range(P1[0], P2[0]):
        for j in range(P1[1], P2[1]):
            img[i][j] = 255 - img[i][j]
    return img

#Recebendo os Pontos
print("Digite os pontos de P1(x1,y1) e P2(x2,y2):")
p1 = []
p2 = []
x1 = int(input("x1: "))
y1 = int(input("y1: "))
p1.append(x1)
p1.append(y1)

#Verificando se os pontos P1 atendem ao tamanho da imagem
while (p1[0] > sizeImg[0] or p1[0] < 0 or p1[1] > sizeImg[1] or p1[1] < 0):
    print("conjunto de pontos inválido, digite novamente")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    p1[0] = x1
    p1[1] = y1

x2 = int(input("x2: "))
y2 = int(input("y2: "))
p2.append(x2)
p2.append(y2)
#Verificando se os pontos P2 atendem ao tamanho da imagem
while (p2[0] > sizeImg[0] or p2[0] < 0 or p2[1] > sizeImg[1] or p2[1] < 0):
    print("conjunto de pontos inválido, digite novamente")
    x2 = int(input("x1: "))
    y2 = int(input("y1: "))
    p2[0] = x2
    p2[1] = y2

#Fazendo a troca dos pontos caso o P2(x,y) possua algum ponto menor que P1(x,y)
if (p1[0] > p2[0]):
    varAux = p1[0]
    p1[0] = p2[0]
    p2[0] = varAux

if (p1[1] > p2[1]):
    varAuxy = p1[1]
    p1[1] = p2[1]
    p2[1] = varAuxy

print(p1,p2)
img2 = spaceNegative(p1,p2,img)
cv.imshow("bielinvertido",img2)
cv.imwrite("../Fotos/bielinvertido.jpg", img2)

cv.waitKey(0)
cv.destroyAllWindows()


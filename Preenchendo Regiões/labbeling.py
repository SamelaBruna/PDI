import cv2 as cv
import numpy as np


# Removendo objetos da borda e contando logo após
def removeAndCount(img):
    sizeImg = np.shape(img)
    numObjects = 0
    for i in range(0, sizeImg[0]):
        for j in range(0, sizeImg[1]):
            if i == 0 or i == sizeImg[0] - 1 or j == 0 or j == sizeImg[1] - 1:
                if img[i][j] == 255:
                    cv.floodFill(img, None, (j, i), 0)
    cv.imshow("noEdge", img)
    cv.imwrite("../Fotos/noEdge.jpg", img)

    for i in range(0, sizeImg[0]):
        for j in range(0, sizeImg[1]):
            if img[i][j] == 255:
                numObjects += 1
                cv.floodFill(img, None, (j, i), numObjects)
    print("Quantidade de bolhas no total: {}".format(numObjects))
    cv.imshow("comTons", img)
    cv.imwrite("../Fotos/Tons.jpg", img)
    return img, numObjects


# Contando quantos obejtos possuem buracos
def holes(img):
    sizeImg = np.shape(img)
    numHoles = 0
    for i in range(0, sizeImg[0]):
        for j in range(0, sizeImg[1]):
            if img[i][j] == 0:
                numHoles += 1
                cv.floodFill(img, None, (j, i), 255)
    print("Quantidade de bolhas com buracos : {}".format(numHoles))
    print("Quantidade de bolhas sem buracos : {}".format(numberObjects - numHoles))


img = cv.imread("../Fotos/bolhas.png", cv.IMREAD_GRAYSCALE)
copy_img = img.copy()

editedImgData = removeAndCount(copy_img)
imgEditada = editedImgData[0]
numberObjects = editedImgData[1]

cv.imshow("antesdoflood", imgEditada)
cv.floodFill(imgEditada, None, (0, 0), 255)
cv.imshow("imgedita", imgEditada)

holes(imgEditada)
cv.imshow("Before", img)
cv.imwrite("../Fotos/Before.jpg", img)
cv.imshow("After", imgEditada)
cv.imwrite("../Fotos/After.jpg", img)
cv.waitKey(0)
cv.destroyAllWindows()

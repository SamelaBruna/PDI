import numpy as np
import sys
import cv2 as cv
import math


img = cv.imread("../Fotos/levi.jpg",cv.IMREAD_GRAYSCALE)
cv.imshow("Original", img)
img = np.float32(img)
sizeImg = np.shape(img)
height = sizeImg[0]
width = sizeImg[1]


yh, yl, c, d0 = 1, 1, 1, 1
dft, dft_M, dft_N = 0, 0, 0
yv, cv1, dv = 0, 0, 0


# Função Filtro Homomorfico.
def filterHomomof():
    global yh, yl, c, d0, dft, dft_M, dft_N
    du = np.zeros(dft.shape, dtype=np.float32)
    for u in range(dft_M):
        for v in range(dft_N):
            du[u, v] = math.sqrt((u - dft_M / 2.0) * (u - dft_M / 2.0) + (v - dft_N / 2.0) * (v - dft_N / 2.0))

    du2 = cv.multiply(du, du) / (d0 * d0)
    re = np.exp(-c * du2)
    H = (yh - yl) * (1 - re) + yl

    # Calculo da DFT inversa
    filtering = cv.mulSpectrums(dft, H, 0)
    filtering = np.fft.ifftshift(filtering)
    filtering = cv.idft(filtering)
    filtering = cv.magnitude(filtering[:, :, 0], filtering[:, :, 1])

    # normalização
    cv.normalize(filtering, filtering, 0, 1, cv.NORM_MINMAX)
    filtrando = np.exp(filtering)
    cv.normalize(filtrando, filtrando, 0, 1, cv.NORM_MINMAX)


    cv.imshow("Filtro Homomorfico", filtering)



def setyl(yv):
    global yl
    yl = yv / 10.0
    if yl > yh:
        yl = yh - 1
    filterHomomof()


def setyh(yv):
    global yh
    yh = yv / 10.0
    if 1 > yh:
        yh = 1
    if yl > yh:
        yh = yl + 1
    filterHomomof()


def setc(cv1):
    global c
    if cv1 == 0:
       cv1 = 1
    c = cv1 / 1000.0
    filterHomomof()


def setd0(dv):
    global d0
    d0 = dv / 10.0
    if d0 == 0:
       d0 = 1
    filterHomomof()


# altura e a largura ideais para realizar a DFT
dft_M = cv.getOptimalDFTSize(height)
dft_N = cv.getOptimalDFTSize(width)


padded = cv.copyMakeBorder(img, 0, dft_M - height, 0, dft_N - width, cv.BORDER_CONSTANT, 0) + 1
padded = np.log(padded)

#Aplicar a DFT
dft = cv.dft(padded, flags=cv.DFT_COMPLEX_OUTPUT)
#Troca os quadrantes
dft = np.fft.fftshift(dft)
img_back = 20 * np.log(cv.magnitude(dft[:, :, 0], dft[:, :, 1]))
esp_freq = np.uint8(img_back)
cv.imshow("Espectro", esp_freq)
cv.imshow("Filtro Homomorfico", img)

#Criação das trackbar
trackbarName = "YL "
cv.createTrackbar(trackbarName, "Filtro Homomorfico", yv, 100, setyl)
trackbarName = "YH "
cv.createTrackbar(trackbarName, "Filtro Homomorfico", yv, 100, setyh)
trackbarName = "C "
cv.createTrackbar(trackbarName, "Filtro Homomorfico", cv1, 100, setc)
trackbarName = "D0 "
cv.createTrackbar(trackbarName, "Filtro Homomorfico", dv, dft_M, setd0)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)
ret, frame = cap.read()
imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
imgHist_previous = cv.calcHist([imgGray],[0],None,[256],[0,256])


if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Our operations on the frame come here
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    imgHist_actual = cv.calcHist([imgGray],[0],None,[256],[0,256])
    sizeImgHis = np.shape(imgHist_actual)
    counterDif = 0
    for i in range(0,sizeImgHis[0]):
        difBetw = imgHist_previous[i] - imgHist_actual[i]
        if difBetw >= 50:
            counterDif += 1
    if counterDif >= 80:
        print("Movimento Detectado ")
    imgHist_previous = imgHist_actual.copy()

    cv.imshow('Actual', imgGray)

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
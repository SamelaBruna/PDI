import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


cap = cv.VideoCapture(0)

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
    histNormal = cv.calcHist([imgGray], [0], None, [256], [0, 256])
    imgEqualized = cv.equalizeHist(imgGray)
    histEqualized = cv.calcHist([imgEqualized],[0],None,[256],[0,256])
    both = np.hstack((imgGray,imgEqualized))

    plt.plot(histNormal, 'r')
    plt.plot(histEqualized, 'b')
    plt.xlim([0, 256])
    plt.show()

    # Display the resulting before and after
    cv.imshow('Left: Normal Image  Right: Equalized Image', both)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
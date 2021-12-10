import cv2 as cv
import numpy as np

media = np.array([[0.1111, 0.1111, 0.1111], [0.1111, 0.1111,0.1111], [0.1111, 0.1111, 0.1111]], dtype=np.float32 )
gauss = np.array([[0.0625, 0.125,  0.0625], [0.125, 0.25,0.125],  [0.0625, 0.125,  0.0625]], dtype=np.float32)
horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
laplacian = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], dtype=np.float32)
boost = np.array([[0, -1, 0], [-1, 5.2, -1], [0, -1, 0]], dtype=np.float32)

def applyFilter(masks, grayedImage, absolute):
  cv.imshow("Original", grayedImage)
  print(absolute)
  grayedImageF32 = np.array(grayedImage, dtype=np.float32)
  result = np.array(grayedImageF32, dtype=np.uint8)

  if (len(masks) == 1):
    frameFiltered = cv.filter2D(grayedImageF32, -1, masks[0])
    if absolute:
      frameFiltered = abs(frameFiltered)

    result = np.array(frameFiltered, dtype=np.uint8)
  else:
    currentFiltered = cv.filter2D(grayedImageF32, -1, masks[0])
    for mask in masks[1:]:
      frameFiltered = cv.filter2D(currentFiltered, -1, mask)
      if absolute:
        frameFiltered = abs(frameFiltered)

    result = np.array(frameFiltered, dtype=np.uint8)

  cv.imshow("Filtered", result)



cap = cv.VideoCapture(0)
mask = [media];
absolute = True

print("\Press the key correspondent to the filter: \n"
        "a - absoluto\n"
        "m - media\n"
        "g - gauss\n"
        "v - vertical\n"
        "h - horizontal\n"
        "l - laplaciano\n"
        "p - gaussiano com laplacian\n"
        "esc - sair\n")

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

  grayedImage = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  key = cv.waitKey(1)
  if key == ord('m'):
    mask = [media]

  elif key == ord('a'):
    absolute = not absolute

  elif key == ord('g'):
    mask = [gauss]

  elif key == ord('h'):
    mask = [horizontal]

  elif key == ord('v'):
    mask = [vertical]

  elif key == ord('l'):
    mask = [laplacian]

  elif key == ord('b'):
    mask = [boost]

  elif key == ord('p'):
    mask = [gauss, laplacian]

  elif key == 27: #esc
    break

  applyFilter(mask, grayedImage, absolute)
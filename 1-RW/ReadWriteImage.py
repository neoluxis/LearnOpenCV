import cv2 as cv
import numpy as np
import sys

img = cv.imread(cv.samples.findFile("icon.jpg"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("saved.png", img)

# cv.destroyAllWindows()
cv.destroyWindow("Display window")

# print(ord("s"))
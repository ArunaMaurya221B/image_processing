import cv2 as cv
import numpy as num

img = cv.imread("j.png")

kernel = num.ones((7,7), num.uint8)

eroded_image = cv.erode(img, kernel, iterations=1)
dilated_image = cv.dilate(img, kernel, iterations=1)

cv.imshow("img", img)
cv.imshow("eroded_image", eroded_image)
cv.imshow("dilated_image", dilated_image)


cv.waitKey(0)
cv.destroyAllWindows()
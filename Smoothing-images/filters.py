import cv2 as cv
import numpy as np


img = cv.imread("yellow.jpg")


kernel = np.ones((7,7), np.float32)/49

blurred = cv.filter2D(img, -1, kernel)
gaussian_blur = cv.GaussianBlur(img, (7,7), 0)
median = cv.medianBlur(img, 7)
bilateral = cv.bilateralFilter(img, 7, 75, 75)


cv.imshow('blurred', blurred)
cv.imshow('gaussian_blur', gaussian_blur)
cv.imshow('median', median)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2
import numpy as np


#reading image
img =cv2.imread("/home/icts/image_processing/dip.34.png")

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#converting to grayscale as colour images give three elements in a tuple, last one for channel
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#taking the number of rows and columns
r, c = gray_img.shape

l=0
count=0
#loop to access individual pixle
for i in range(0, r):
	for j in range(0, c):
		if gray_img[i][j] == 0 and gray_img[i][j-1]==255:
			count = count+1
			#cv2.imshow('image', gray_img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
			curr_x = i
			curr_y = j
			while gray_img[curr_x][curr_y] != 255 :
				l=l+1 #length
				curr_y=curr_y+1

			temp_x = i+l
			temp_y = j+l
			area = l*l
			perimeter = 4*l
			print 'Length: ', l, 'Area: ', area, 'Perimeter: ', perimeter
			"""print raw_input("Length of {} = {}".format(count, l))
			print raw_input("Area of {} = {} ".format(count, area))
			print raw_input("Perimeter of {} = {}".format(count, 4*l))"""
			for k in range(i, temp_x):
				for l in range(j, temp_y):
					#print l
					gray_img[k][l]=255


print raw_input("Total number of squares detected: {}".format(count))
cv2.imshow('image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
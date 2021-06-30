'''
install these packages first :
cv2
'''
import cv2

img = cv2.imread('./pic.jpg')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255-gray_image
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)
inverted_blurred_image = 255-blurred_img
pincel_sketch_IMG = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

cv2.imshow('Original Image', pincel_sketch_IMG)
cv2.waitKey(0)

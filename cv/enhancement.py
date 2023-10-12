import cv2
image = cv2.imread('low_contrast.jpg')

alpha = 1.5
beta = 0.5
result = cv2.addWeighted(image, alpha, image, 0, beta)
cv2.imshow('orig', image)
cv2.imshow('Image', result)
cv2.waitKey(0)

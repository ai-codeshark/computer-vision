import cv2
import numpy as np

# Load an image
img = cv2.imread('blurred.jpg')

# Generate a blur kernel
kernel_size = 15
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)

# Blur the image
blurred = cv2.filter2D(img, -1, kernel)

# Deblur the image using Richardson-Lucy deconvolution
iterations = 30
result = cv2.deconvolve(blurred.astype(float), kernel.astype(float))[0]
for i in range(iterations):
    result *= cv2.filter2D(blurred.astype(float) /
                           cv2.filter2D(result, -1, kernel), -1, kernel)
result = np.clip(result, 0, 255).astype(np.uint8)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)

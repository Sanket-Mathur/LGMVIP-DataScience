# LetsGrowMore - Virtual Internship Program
# Beginner Level Task - Task 4
# Image to Pencil Sketch with Python
  
# Submitted By - Sanket Mathur

import cv2.cv2

# reading the image and converting it to RGB
img = cv2.imread('./img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# grayscale version of image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#inverting the grayscale image
inverted = 255 - gray

# creating trackbar for kernel size
cv2.namedWindow('Parameters')
cv2.cv2.resizeWindow('Parameters', 640, 80)
cv2.createTrackbar('Kernel', 'Parameters', 1, 99, lambda a: None)
cv2.setTrackbarMin('Kernel', 'Parameters', 1)

while True:
    # getting trackbar position
    kernel = cv2.getTrackbarPos('Kernel', 'Parameters')
    if kernel % 2 == 0:
        kernel += 1
    cv2.setTrackbarPos('Kernel', 'Parameters', kernel)

    # inverting blur image of the inverted image
    KERNAL_SIZE = (kernel, kernel)
    blur = cv2.GaussianBlur(inverted, KERNAL_SIZE, 0)
    inverted_blur = 255 - blur

    # creating the sketch by dividing grayscaled image with inverted blurred image
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    cv2.imshow('Pencil Sketch', sketch)
    
    # exit on 'q' key
    if cv2.waitKey(1) &0xFF == ord('q'):
        break

cv2.destroyAllWindows()
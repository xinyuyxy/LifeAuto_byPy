# TO REMOVE WHITE BACKGROUND AND CHANGE TO TRANSPARANT
# PNG IMAGE HAS THE FOURTH CHANNEL TO DEFINE TRANSPARANCY

import cv2 as cv
import matplotlib.pyplot as plt

# OPEN SROURCE IMG
img = cv.imread(r"C:\Users\h638206\Desktop\Picture5.png", 1)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# DEFINE BACKGROUND THRESHOLD
_, alpha = cv.threshold(img_grey, 200, 255, cv.THRESH_BINARY_INV)

# ADD ALPHA CHANNEL TO SOURCE IMG
b, g, r = cv.split(img)
rgba = [b, g, r, alpha]
dst = cv.merge(rgba, 4)

# SAVE AS PNG IMG
cv.imwrite(r"C:\Users\h638206\Desktop\Picture5-1.png", dst)
plt.imshow(img)

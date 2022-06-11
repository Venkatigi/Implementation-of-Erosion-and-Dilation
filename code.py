import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=np.zeros((100,500),dtype='uint8')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

cv2.putText(img1,' VENKATESH E ',(10,70),font,2,(25),5,cv2.LINE_AA)
plt.imshow(img1,cmap='gray')

kernel1=cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7))

img_erode=cv2.erode(img1,kernel1)
plt.imshow(img_erode,cmap='gray')

img_dilate=cv2.dilate(img1,kernel1)
plt.imshow(img_dilate,cmap='gray')
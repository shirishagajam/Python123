# importing cv2 
import cv2 
import numpy as np

rect = np.ones((600,800,3),dtype=np.uint8)*255

#frame, upper_left, bottom_right, bgr, thickness of rectangle border
cv2.rectangle(rect, (int(800/2),0),(799, int(800/2)),(0, 255, 0), 2)

cv2.imshow('image', rect)
cv2.waitKey()
cv2.destroyAllWindows()
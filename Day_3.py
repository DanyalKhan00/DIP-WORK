

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# bright = cv2.add(img,-150)
# cv2.imshow("Original Image : ",img)
# cv2.imshow("Bright Image : ",bright)
# cv2.waitKey(0)

#(2):
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# bright = 155 - img
# cv2.imshow("Original Image : ",img)
# cv2.imshow("Bright Image : ",bright)
# cv2.waitKey(0)

#(3)
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# bright =cv2.blur(img,(3,3))
# cv2.imshow("Original Image : ",img)
# cv2.imshow("Bright Image : ",bright)
# cv2.waitKey(0)

#(4) : 
# import numpy as np
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# kernel = np.array([
#     [0, -1, 0],
#     [-1, 5, -1],
#     [0, -1, 0]
# ])

# sharp = cv2.filter2D(img, -1, kernel)
# cv2.imshow("Original Image : ",img)
# cv2.imshow("Bright Image : ",sharp)
# cv2.waitKey(0)
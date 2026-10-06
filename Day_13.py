# 1
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.ones((3,3),np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Opening : ", opening)
# cv2.waitKey(0)

#2 :

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.ones((3,3),np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Opening : ", closing)
# cv2.waitKey(0)

#3 :
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.ones((3,3),np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Opening : ", opening)
# cv2.imshow("Closing : ", closing)
# cv2.waitKey(0)


#4 : 

# import cv2
# import numpy as np
# img = cv2.imread("image.jpg", 0)
# kernel3 = np.ones((3, 3), np.uint8)
# kernel5 = np.ones((5, 5), np.uint8)
# opening3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel3)
# opening5 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel5)
# cv2.imshow("Original", img)
# cv2.imshow("Opening 3x3", opening3)
# cv2.imshow("Opening 5x5", opening5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
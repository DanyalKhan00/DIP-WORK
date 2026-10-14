# All About Color Image processing  ....
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# blue = img[:, :, 0]
# green = img[:, :, 1]
# red = img[:, :, 2]
# result = np.zeros_like(img)
# mask = (red >= 100) & (red <= 200)
# result[mask] = img[mask]
# cv2.imshow("Original Image", img)
# cv2.imshow("Color Slicing", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#2
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# blue = img[:, :, 0]
# green = img[:, :, 1]
# red = img[:, :, 2]
# result = np.zeros_like(img)
# mask =blue > 150
# result[mask] = img[mask]
# cv2.imshow("Original Image", img)
# cv2.imshow("Color Slicing", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


 #3
 
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 002.jfif")
# blue = img[:, :, 0]
# green = img[:, :, 1]
# red = img[:, :, 2]
# result = np.zeros_like(img)
# mask = (red > 150) & (red > green) & (red > blue)
# result[mask] = img[mask]
# cv2.imshow("Original Image", img)
# cv2.imshow("Red Dominant Slicing", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
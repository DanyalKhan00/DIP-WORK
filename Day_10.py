# All About Gradient Filtering ..
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg" , 0)
# gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
# gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
# mag = np.sqrt(gx**2 + gy**2)
# output = cv2.convertScaleAbs(mag)  
# cv2.imshow("Original", img)
# cv2.imshow("Gradient", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Robert Mask
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg" , 0)
# mask_x = np.array([[1, 0],
#                    [0, -1]])
# mask_y = np.array([[0, 1],
#                    [-1, 0]])
# gx = cv2.filter2D(img, cv2.CV_64F, mask_x)
# gy = cv2.filter2D(img, cv2.CV_64F, mask_y)
# output = np.sqrt(gx**2 + gy**2)
# output = np.clip(output, 0, 255).astype(np.uint8)
# cv2.imshow("Original", img)
# cv2.imshow("Roberts", output)
# cv2.waitKey(0)

# Prewitt Mask

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg" , 0)
# mask_x = np.array([[-1, 0, 1],
#                    [-1, 0, 1],
#                    [-1, 0, 1]])
# mask_y = np.array([[-1,-1,-1],
#                    [0,0,0],
#                    [1,1,1]])
# gx = cv2.filter2D(img, cv2.CV_64F, mask_x)
# gy = cv2.filter2D(img,cv2.CV_64F , mask_y)
# output = np.sqrt(gx**2 + gy**2)
# output = np.clip(output, 0, 255).astype(np.uint8)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Prewitt X", cv2.convertScaleAbs(gx))
# cv2.imshow("Prewitt Y", cv2.convertScaleAbs(gy))
# cv2.imshow("Final Edge", output)
# cv2.waitKey(0)

# Sobel Mask .......

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg" , 0)
# mask_x = np.array([[-1, 0, 1],
#                    [-2, 0, 2],
#                    [-1, 0, 1]])

# mask_y = np.array([[-1, -2, -1],
#                    [ 0,  0,  0],
#                    [ 1,  2,  1]])
# gx = cv2.filter2D(img, cv2.CV_64F,mask_x)
# gy = cv2.filter2D(img, cv2.CV_64F, mask_y)
# output = np.sqrt(gx**2 + gy**2)
# output = np.clip(output, 0, 255).astype(np.uint8)
# cv2.imshow("ORIGNAL IMAGE : ", img)
# cv2.imshow("Sobel X", cv2.convertScaleAbs(gx))
# cv2.imshow("Sobel Y",cv2.convertScaleAbs(gy))
# cv2.imshow("Final Sobel ",output)
# cv2.waitKey(0)


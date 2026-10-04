# All About Morphologicall Image Processing ........
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.ones((3, 3), np.uint8)
# eroded = cv2.erode(img, kernel)
# cv2.imshow("Original", img)
# cv2.imshow("Eroded", eroded)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.zeros((7,7), np.uint8)
# eroded = cv2.erode(img , kernel)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Eroded Image : ", eroded)
# cv2.waitKey(0)

#Q3.Eroded image Using 5 x 5
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# kernel = np.ones((5,5), np.uint8)
# eroded = cv2.erode(img, kernel)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Eroded Image : ", eroded)
# cv2.waitKey(0)

#Q2: Eroded Image Using 3 x 3
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)
# kernel = np.ones((3,3), np.uint8)
# eroded = cv2.erode(img, kernel)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Eroded Image : ", eroded)
# cv2.waitKey(0)

# Q3: Eroded Image Using 3 x 3 & 5 x 5
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images (2).jfif")
# img = cv2.resize(img, (300, 300))
# kernel1 = np.ones((3,3),np.uint8)
# kernel2 = np.ones((5,5),np.uint8)
# print()
# eroded1 = cv2.erode(img, kernel1)
# eroded2 = cv2.erode(img, kernel2)
# cv2.imshow("ORIGNAL IMAGE : ", img)
# cv2.imshow("ERODED1 IMAGE : ", eroded1)
# cv2.imshow("ERODED2 IMAGE : ", eroded2)
# cv2.waitKey(0)

#Q4:
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# kernel = np.array([
#     [1, 1, 1],
#     [0, 1, 0],
#     [0, 1, 0]
# ], dtype=np.uint8)
# eroded= cv2.erode(img , kernel)
# cv2.imshow("ORIGINAL IMAGE : ", img)
# cv2.imshow("ERODED IMAGE : ",eroded)
# cv2.waitKey(0)

#Q5:
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# kernel = np.ones((3, 3), np.uint8)
# eroded = cv2.erode(img, kernel)
# cv2.imshow("Original Image", img)
# cv2.imshow("Eroded Image", eroded)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
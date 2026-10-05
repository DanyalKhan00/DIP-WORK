# All About Dilation  ...
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.ones((3,3), np.uint8)
# dilate = cv2.dilate(img, kernel)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Dilate Image : ", dilate)
# cv2.waitKey(0)

#
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# img = cv2.resize(img, (300, 300))
# kernel1 = np.ones((3,3), np.uint8)
# kernel2 = np.ones((5,5), np.uint8)
# print()
# dilate1 = cv2.dilate(img , kernel1)
# dilate2 = cv2.dilate(img , kernel2)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("3 x 3 kernel : ", dilate1)
# cv2.imshow("5 x 5 kernel : ", dilate2)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img =cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# kernel = np.array([ [0, 1, 0],
#     [1, 1, 1],
#     [0, 1, 0]
# ], dtype=np.uint8)
# dilate = cv2.dilate(img , kernel)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Dilate Image : ", dilate)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# kernel = np.ones((3,3), np.uint8)

# erode = cv2.erode(img , kernel)
# dilate = cv2.dilate(img, kernel )
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Erode Image : ",erode)
# cv2.imshow("Dilate Image : ", dilate)
# cv2.waitKey(0)
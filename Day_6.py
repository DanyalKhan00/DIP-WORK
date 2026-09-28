# All About Filtering    ................ ?

#       Average Filtering ......
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Screenshots\\Screenshot (488).png")
# kernel = np.ones((3, 3), np.float32) / 9
# result = cv2.filter2D(img, -1, kernel)
# cv2.imshow("Original", img)
# cv2.imshow("Averaging Filter", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Median Filter ......
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# result = cv2.medianBlur(img, 3)
# cv2.imshow("Original", img)
# cv2.imshow("Median Filter", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Maximum Filter ...


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# kernel = np.ones((3, 3), np.uint8)
# result = cv2.dilate(img, kernel)
# cv2.imshow("Original", img)
# cv2.imshow("Maximum Filter", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Minimum Filter ...
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# kernel = np.ones((3, 3), np.uint8)
# result = cv2.erode(img, kernel)
# cv2.imshow("Original", img)
# cv2.imshow("Minimum Filter", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
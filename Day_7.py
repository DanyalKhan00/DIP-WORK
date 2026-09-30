# All About Correlation ......

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# kernel = np.array([[1, 0, -1],
#                    [1, 0, -1],
#                    [1, 0, -1]])
# result = cv2.filter2D(img, -1, kernel)
# cv2.imshow("Original Image", img)
# cv2.imshow("Correlation", result)
# cv2.waitKey(0)
#cv2.destroyAllWindows()
# All About Convolution ....

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# kernel = np.array([[1, 0, -1],
#                    [1, 0, -1],
#                    [1, 0, -1]])
# rotated = cv2.flip(kernel, -1)
# result = cv2.filter2D(img, -1, rotated)
# cv2.imshow("Original Image", img)
# cv2.imshow("Convolution", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# image = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# output = cv2.blur(image, (3, 3))
# cv2.imshow("Original", image)
# cv2.imshow("Averaged", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# image = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)
# output = cv2.GaussianBlur(image, (5, 5), 0)
# cv2.imshow("Original", image)
# cv2.imshow("Gaussian Filter", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
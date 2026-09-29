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

import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
kernel = np.array([[1, 0, -1],
                   [1, 0, -1],
                   [1, 0, -1]])
rotated = cv2.flip(kernel, -1)
result = cv2.filter2D(img, -1, rotated)
cv2.imshow("Original Image", img)
cv2.imshow("Convolution", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
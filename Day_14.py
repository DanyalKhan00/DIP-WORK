# All About Hit or Miss Transformation ........

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
# binary = (img > 127).astype(np.uint8)
# kernel = np.array([
#     [-1, -1, -1],
#     [-1,  1, -1],
#     [-1, -1, -1]
# ], dtype=np.int8)
# result = cv2.morphologyEx(binary, cv2.MORPH_HITMISS, kernel)
# cv2.imshow("Binary : ", binary * 255)
# cv2.imshow("Resulted Image : ", result * 255)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.png",0)
# binary = (img > 127).astype(np.uint8)
# kernel = np.array([
#     [-1,  1, -1],
#     [-1,  1, -1],
#     [-1, -1, -1]
# ], dtype=np.int8)
# result = cv2.morphologyEx(
#     binary,
#     cv2.MORPH_HITMISS,
#     kernel
# )
# cv2.imshow("Original", binary * 255)
# cv2.imshow("Endpoint", result * 255)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#
import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)
binary = (img > 127).astype(np.uint8)
kernel = np.array([
    [-1, -1, -1, -1, -1],
    [ 1,  1,  1,  1,  1],
    [-1, -1, -1, -1, -1]
], dtype=np.int8)
result = cv2.morphologyEx(binary,cv2.MORPH_HITMISS,kernel)
cv2.imshow("Orignal : ", img)
cv2.imshow("Binary : ", binary * 255)
cv2.imshow("Horizontal Pattern : ", result * 255)
cv2.waitKey(0)

#
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
# binary = (img > 127).astype(np.uint8)
# kernel = np.array([
#     [ 1, -1, -1],
#     [ 1, -1, -1],
#     [ 1,  1,  1]
# ], dtype=np.int8)
# result = cv2.morphologyEx(binary,cv2.MORPH_HITMISS,kernel)
# cv2.imshow("Orignal Image : ",binary * 255)
# cv2.imshow("Result : ", result * 255)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
# binary = (img > 127).astype(np.uint8)
# kernel = np.array([
#     [ 1,  1, -1],
#     [ 1, -1, -1],
#     [-1, -1, -1]
# ], dtype=np.int8)
# result = cv2.morphologyEx(binary,cv2.MORPH_HITMISS,kernel)
# cv2.imshow("Orignal Image : ",binary * 255)
# cv2.imshow("Result : ", result * 255)
# cv2.waitKey(0)


import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
binary = (img > 127).astype(np.uint8)
kernel = np.array([
      [ 0, -1,  0],
    [ 1,  1,  1],
    [ 0, -1,  0]
], dtype=np.int8)
result = cv2.morphologyEx(binary,cv2.MORPH_HITMISS,kernel)
cv2.imshow("Orignal Image : ",binary * 255)
cv2.imshow("Result : ", result * 255)
cv2.waitKey(0)
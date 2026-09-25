# # All About Piece Wise Linear Transformation ........\
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# output = np.zeros_like(img)
# output[(img >= 100) & (img <= 150)] = 255
# cv2.imshow("Original Image", img)
# cv2.imshow("Intensity Level Slicing", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# out = np.zeros_like(img)
# out[(img > 90)& (img <= 130)] = 255
# cv2.imshow("Orignal Img " , img)
# cv2.imshow("Intensity Img ", out)
# cv2.waitKey(0)


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# output = np.zeros_like(img)
# output[(img > 80 )& (img <= 150)] = 255
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Intensity Slicing : ", output)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# output =img.copy()
# output[(img > 100 )& (img <= 180)] = 255
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Intensity Slicing : ", output)
# cv2.waitKey(0)

import cv2
import numpy as np
img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
output = np.zeros_like(img)
condtion = ((img >= 30 )& (img <=80) | (img >= 100) & (img <= 200)) 
output[condtion] = 255
cv2.imshow("Original Image : ", img)
cv2.imshow("Intensity Slicing : ", output)
cv2.waitKey(0)
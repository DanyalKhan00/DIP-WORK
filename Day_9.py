# All About LapLacian Filter ...

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# output = cv2.convertScaleAbs(laplacian)
# cv2.imshow("Original", img)
# cv2.imshow("Laplacian", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
  


import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)

if img is None:
    print("Error: Image not found!")
else:
    laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize=1)

    sharpened = img.astype(np.float32) - laplacian

    sharpened = np.clip(sharpened, 0, 255)
    sharpened = sharpened.astype(np.uint8)

    cv2.imshow("Original", img)
    cv2.imshow("Sharpened", sharpened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# All About LapLacian Filter ...

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)
# laplacian = cv2.Laplacian(img, cv2.CV_64F)
# output = cv2.convertScaleAbs(laplacian)
# cv2.imshow("Original", img)
# cv2.imshow("Laplacian", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
  


# import cv2
# import numpy as np

# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg",0)

# if img is None:
#     print("Error: Image not found!")
# else:
#     laplacian = cv2.Laplacian(img, cv2.CV_32F, ksize=1)

#     sharpened = img.astype(np.float32) - laplacian

#     sharpened = np.clip(sharpened, 0, 255)
#     sharpened = sharpened.astype(np.uint8)

#     cv2.imshow("Original", img)
#     cv2.imshow("Sharpened", sharpened)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# Gaussian Filter ...

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# Gaussian = cv2.GaussianBlur(img ,(5,5),0)
# cv2.imshow("Orignal Image : ",img)
# cv2.imshow("Gaussian Image :",Gaussian)
# cv2.waitKey(0)



# Laplacian Filter


# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
# lap = cv2.Laplacian(img , cv2.CV_64F)
# lap = cv2.convertScaleAbs(lap)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Laplacian Image : ", lap)
# cv2.waitKey(0)

# Gaussian Over Laplasian ...
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# Gaussian= cv2.GaussianBlur(img, (5,5), 0)
# lap = cv2.Laplacian(Gaussian,cv2.CV_64F)
# lap = cv2.convertScaleAbs(lap)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Gaussian Image : ", Gaussian)
# cv2.imshow("Laplacian Image : ", lap)
# cv2.waitKey(0)
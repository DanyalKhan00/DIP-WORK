# All About Thickening and Thinning 
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\downloads.png",0)
# binary = (img > 127).astype(np.uint8) * 255
# thin = cv2.ximgproc.thinning(binary)
# cv2.imshow("Original Image : ", binary)
# cv2.imshow("Thinning Image : ", thin)
# cv2.waitKey(0)


#2
# import cv2
# import numpy as np
# img=cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download4.jfif",0)
# img = cv2.resize(img, (300, 300))
# binary = (img > 127).astype(np.uint8) * 255
# thin = cv2.ximgproc.thinning(binary)
# cv2.imshow("Orignal Image :",img)
# cv2.imshow("Binary : ", binary)
# cv2.imshow("Thinning Image : ", thin)
# cv2.waitKey(0)


#3
# import cv2
# import numpy as np
# img1=cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download1.jfif",0)
# img2=cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download2.jfif",0)
# img1 = cv2.resize(img1, (300, 300))
# img2 = cv2.resize(img2, (300, 300))
# binary1 = (img1 > 127).astype(np.uint8) * 255
# binary2 = (img2 > 127).astype(np.uint8) * 255
# thin1 = cv2.ximgproc.thinning(binary1)
# thin2 = cv2.ximgproc.thinning(binary2)
# cv2.imshow("Letter - Original", binary1)
# cv2.imshow("Letter - Thinned", thin1)

# cv2.imshow("Shape - Original", binary2)
# cv2.imshow("Shape - Thinned", thin2)
# cv2.waitKey(0)

#  All About Thickening Of image ...
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\sss.png", 0)
# binary = (img > 127).astype(np.uint8) * 255
# complement = cv2.bitwise_not(binary)
# thin = cv2.ximgproc.thinning(complement)
# thick = cv2.bitwise_not(thin)
# cv2.imshow("Original Image", binary)
# cv2.imshow("Thickened Image", thick)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#2

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images22.jfif", 0)
# binary = (img > 127).astype(np.uint8) * 255
# complement = cv2.bitwise_not(binary)
# thin = cv2.ximgproc.thinning(complement)
# thick = cv2.bitwise_not(thin)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Thickend Image : ", thick)
# cv2.waitKey(0)
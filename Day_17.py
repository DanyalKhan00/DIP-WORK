# All About Color Image .......
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\colors.png")
# blue , green ,red = cv2.split(img)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Red Channel : ", red)
# cv2.imshow("Green Channel : ", green)
# cv2.imshow("Blue Channel : ", blue)
# cv2.waitKey(0)


#2
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download.jfif")
# resize = cv2.resize(img,(250,250))
# gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# cv2.imshow("RGB IMAGE : ", img)
# cv2.imshow("GRAY IMAGE : ", gray)
# cv2.waitKey(0)


#3

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\sss1.tif")
# resize = cv2.resize(img,(250,250))
# ct = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# cv2.imshow("Original Image", img)
# cv2.imshow("BGR Image", ct)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#4
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download2.jfif")
# hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("HUE Channel : ", h)
# cv2.imshow("Saturation Channel : ", s)
# cv2.imshow("Value Channel : ", v)
# cv2.waitKey(0)


# Separate Red, Green, and Blue channels

# import cv2
# import numpy as np
# img =  cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\img.jpg")
# blue , green , red = cv2.split(img)
# zero= np.zeros_like(blue)
# red_img = cv2.merge([zero, zero, red])
# green_img = cv2.merge([zero, green, zero])
# blue_img = cv2.merge([zero, zero, blue])

# cv2.imshow("Image : ", img)
# cv2.imshow("Red_Channel  : ", red_img)
# cv2.imshow("Green Channel : ", green_img)
# cv2.imshow("Blue Channel  : ", blue_img)
# cv2.waitKey(0)


# 

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\colors.png")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower1 = np.array([0, 100, 100])
# upper1 = np.array([10, 255, 255])
# lower2 = np.array([170, 100, 100])
# upper2 = np.array([179, 255, 255])
# mask1 = cv2.inRange(hsv, lower1, upper1)
# mask2 = cv2.inRange(hsv, lower2, upper2)
# mask = cv2.bitwise_or(mask1, mask2)
# result = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow("Original Image", img)
# cv2.imshow("Red Mask", mask)
# cv2.imshow("Detected Red Color", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 

# import cv2
# import numpy as np

# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\colors.png")

# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# red, green, blue = cv2.split(rgb)

# reconstructed = cv2.merge([red, green, blue])

# cv2.imshow("Original Image", img)
# cv2.imshow("Reconstructed Image", cv2.cvtColor(reconstructed, cv2.COLOR_RGB2BGR))

# cv2.waitKey(0)
# cv2.destroyAllWindows()
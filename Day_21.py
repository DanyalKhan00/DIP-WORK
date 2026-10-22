# All About Smoothing Of Image .......


# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 00.jfif")
# smo =cv2.blur(img,(5,5))
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Smoothed Image : ",smo)
# cv2.waitKey(0)


# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# smo =cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Smoothed Image : ",smo)
# cv2.waitKey(0)



# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 002.jfif")
# smo =cv2.medianBlur(img,5)
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Smoothed Image : ",smo)
# cv2.waitKey(0)

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# h,s,v = cv2.split(hsv)
# smooth_v = cv2.GaussianBlur(v, (5, 5), 0)
# new_hsv = cv2.merge((h, s, smooth_v))
# result = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Smoothed Image : ", result)
# cv2.waitKey(0)
                                                                                                                                               





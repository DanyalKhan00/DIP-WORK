# All About Color Transformation .....
# (1) : 

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
# process = img * 0.7
# process = process.astype(np.uint8)
# cv2.imshow("Orignal Image : ", cv2.cvtColor(img , cv2.COLOR_RGB2BGR))
# cv2.imshow("Process Image : ", cv2.cvtColor(process , cv2.COLOR_RGB2BGR))
# cv2.waitKey(0)

#(2)  :

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# hsv= cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
# h,s,v = cv2.split(hsv)
# v = v * 0.7
# v = v.astype(np.uint8)
# result = cv2.merge((h,s,v))
# processed = cv2.cvtColor(result , cv2.COLOR_HSV2BGR)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Processed image : ", processed)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 002.jfif")
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# processed = rgb * 0.5
# processed = processed.astype(np.uint8)
# print("Original RGB Pixel:", rgb[100, 100])
# print("Processed RGB Pixel:", processed[100, 100])
# cv2.imshow("Original Image", cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
# cv2.imshow("Processed Image", cv2.cvtColor(processed, cv2.COLOR_RGB2BGR))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Color Complement .........


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 00.jfif")
# complement = 255 - img
# cv2.imshow("Original Image : ", img)
# cv2.imshow("Complemented Image : ", complement)
# cv2.waitKey(0)


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cmy = 255 - rgb
# cmy_display = cv2.cvtColor(cmy, cv2.COLOR_RGB2BGR)
# cv2.imshow("Original Image", img)
# cv2.imshow("CMY Image", cmy_display)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
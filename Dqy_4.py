# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif")
# neg = img - 100
# cv2.imshow("ORIGINAL IMAGE : ", img)
# cv2.imshow("TRANSFORMATION IMAGE : ", neg)
# cv2.waitKey(0)


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif", 0)
# max_intensity = np.max(img)
# c = 255 / np.log(1 + max_intensity)
# log_image = c * np.log(1 + img)
# log_image = np.uint8(log_image)
# original_min = np.min(img)
# original_max = np.max(img)
# log_min = np.min(log_image)
# log_max = np.max(log_image)
# print("Maximum Intensity:", max_intensity)
# print("Constant c:", c)
# print("Original Minimum:", original_min)
# print("Original Maximum:", original_max)
# print("Log Image Minimum:", log_min)
# print("Log Image Maximum:", log_max)
# cv2.imshow("Original Image", img)
# cv2.imshow("Log Transformation", log_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Log Transformation  .............
# import cv2
# import numpy as np

# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images.jfif",0)

# c = 255 / np.log(1 + np.max(img))

# log_image = c * np.log(1 + img)

# log_image = np.uint8(log_image)

# cv2.imshow("Original Image", img)
# cv2.imshow("Log Transformation", log_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Gammma Law Transformation ...
 
# import cv2
# import numpy as np

# img = cv2.imread(r"C:\Users\Officer Danyal\Pictures\images.jfif", 0)

# # Convert image to float
# img = img / 255.0

# gamma = 0.5

# # Power-Law Transformation
# power_image = np.power(img, gamma)

# # Convert back to 0-255
# power_image = np.uint8(power_image * 255)

# cv2.imshow("Original Image", np.uint8(img * 255))
# cv2.imshow("Power Law Transformation", power_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Contrast Stretching ...


# import cv2
# import numpy as np

# img = cv2.imread(r"C:\Users\Officer Danyal\Pictures\images.jfif", 0)

# # Find minimum and maximum intensity
# r_min = np.min(img)
# r_max = np.max(img)

# # Apply contrast stretching
# stretched = ((img - r_min) / (r_max - r_min)) * 255

# # Convert to 8-bit image
# stretched = np.uint8(stretched)

# cv2.imshow("Original Image", img)
# cv2.imshow("Contrast Stretched Image", stretched)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2

# img = cv2.imread(r"C:\Users\Officer Danyal\Pictures\images.jfif", 0)

# # Set threshold value
# threshold = 127

# # Apply thresholding
# _, binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

# cv2.imshow("Original Image", img)
# cv2.imshow("Thresholded Image", binary)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
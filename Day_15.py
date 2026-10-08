# All About Boundary Extraction .....

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
# _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3,3),np.uint8)
# eroded = cv2.erode(binary, kernel)
# boundry = binary - eroded
# cv2.imshow("Oringal Image : ", binary)
# cv2.imshow("Boundary Extracted Image : ", boundry)
# cv2.waitKey(0)

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif",0)
# _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# kernel = np.ones((5,5),np.uint8)
# eroded = cv2.erode(binary, kernel)
# boundry = binary - eroded
# cv2.imshow("Oringal Image : ", binary)
# cv2.imshow("Eroded Image : ", eroded)
# cv2.imshow("Boundary Extracted Image : ", boundry)
# cv2.waitKey(0)


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# kernel = np.ones((3, 3), np.uint8)
# eroded = cv2.erode(binary, kernel)
# boundary = binary - eroded
# cv2.imshow("Original Color Image", img)
# cv2.imshow("Binary Image", binary)
# cv2.imshow("Boundary", boundary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# All About Region or Hole Filling ......
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif", 0)
# binary = (img > 127).astype(np.uint8)
# filled = binary.copy()
# h, w = binary.shape
# mask = np.zeros((h + 2, w + 2), np.uint8)
# cv2.floodFill(filled, mask, (0, 0), 1)
# holes = 1 - filled
# result = binary | holes
# cv2.imshow("Original", binary * 255)
# cv2.imshow("Hole Filled", result * 255)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Read image
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\imag.jfif", 0)

# # Convert to binary
# binary = (img > 127).astype(np.uint8)

# # Create a copy
# flood = binary.copy()

# # Create flood-fill mask
# h, w = binary.shape
# mask = np.zeros((h + 2, w + 2), np.uint8)

# # Flood fill background
# cv2.floodFill(flood, mask, (0, 0), 1)

# # Invert the flood-filled image
# holes = 1 - flood

# # Combine original object with holes
# filled = binary | holes

# # Display
# cv2.imshow("Original Ring", binary * 255)
# cv2.imshow("Filled Ring", filled * 255)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
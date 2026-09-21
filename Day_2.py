
# All About 2nd Chapter .......
# Question 1: 

# import numpy as np
# x = np.array([[1,2,3,4,5],
#               [6,7,8,9,0],
#               [11,12,13,14,15],
#               [16,17,18,18,20],
#               [21,22,23,24,25]])
# print("Image",x)
# print("Shape",x.shape)
# print("No Of Pixel",x.size)
# print("Data Type ",x.dtype)

# Q2: ............
# import numpy as np
# img = np.array([
#     [1, 2, 3, 4, 5, 6],
#     [7, 8, 9, 10, 11, 12],
#     [13, 14, 15, 16, 17, 18],
#     [19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30],
#     [31, 32, 33, 34, 35, 36]
# ])
# sam = img[::2,::2]
# print("Sampling : ", sam)


# Q3: .................... ?
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Gray Image : ", gray)
# cv2.waitKey(0)

# Q4: ...........
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# sam = img[::1, ::1]
# cv2.imshow("Sampling ", sam)
# cv2.imshow("Orignal Image : ", img)
# print("Shape Of S.I", img.shape)
# print("Shape Of O.I",sam.shape)
# cv2.waitKey(0)
# Q5 : ................
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# sam = img[::1, ::1]
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray ", gray)
# cv2.imshow("Sampling ", sam)
# cv2.imshow("Orignal Image : ", img)
# print("Shape Of S.I", img.shape)
# print("Shape Of O.I",sam.shape)
# quan = (gray//32)*32
# cv2.imshow("Quantize Image : ",quan)
# cv2.waitKey(0)

# Q6 : 
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp")
# nearest = cv2.resize(
#     img,
#     (400, 400),
#     interpolation=cv2.INTER_NEAREST
# )
# bilinear = cv2.resize(
#     img,
#     (400, 400),
#     interpolation=cv2.INTER_LINEAR
# )
# bicubic = cv2.resize(
#     img,
#     (400, 400),
#     interpolation=cv2.INTER_CUBIC
# )
# cv2.imshow("Nearest Neighbor", nearest)
# cv2.imshow("Bilinear", bilinear)
# cv2.imshow("Bicubic", bicubic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# (7): .................

import cv2
img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\Class.webp" , 0)
# Select pixel
x = 100
y = 100
print("Pixel value:", img[y, x])
# 4-neighbors
print("\n4-Neighbors:")
print("Top:", img[y-1, x])
print("Bottom:", img[y+1, x])
print("Left:", img[y, x-1])
print("Right:", img[y, x+1])
# Diagonal neighbors
print("\nDiagonal Neighbors:")
print("Top-Left:", img[y-1, x-1])
print("Top-Right:", img[y-1, x+1])
print("Bottom-Left:", img[y+1, x-1])
print("Bottom-Right:", img[y+1, x+1])
# 8-neighbors
print("\n8-Neighbors:")
print(
    img[y-1:y+2, x-1:x+2]
)
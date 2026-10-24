# All About Local Binary Pattern (LBP)


# matrix = [
#     [10, 20, 30],
#     [5, 15, 25],
#     [0, 10, 40]
# ]
# center = matrix[1][1]
# neighbors = [
#     matrix[0][0], matrix[0][1], matrix[0][2],
#     matrix[1][2], matrix[2][2], matrix[2][1],
#     matrix[2][0], matrix[1][0]
# ]
# binary = ""
# for pixel in neighbors:
#     if pixel >= center:
#         binary += "1"
#     else:
#         binary += "0"
# lbp_value = int(binary, 2)
# print("Center Pixel:", center)
# print("Binary Pattern:", binary)
# print("LBP Value:", lbp_value)

# import cv2
# import numpy as np

# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images (3).jfif",0)
# if img is None:
#     print("Image not found!")
# else:
#     height, width = img.shape

#     lbp = np.zeros((height, width), dtype=np.uint8)

#     for i in range(1, height - 1):
#         for j in range(1, width - 1):

#             center = img[i, j]
#             value = 0

#             neighbors = [
#                 (-1, -1), (-1, 0), (-1, 1),
#                 (0, 1), (1, 1), (1, 0),
#                 (1, -1), (0, -1)
#             ]

#             for bit, (dx, dy) in enumerate(neighbors):
#                 if img[i + dx, j + dy] >= center:
#                     value += 1 << (7 - bit)

#             lbp[i, j] = value

#     cv2.imshow("Original Image", img)
#     cv2.imshow("LBP Image", lbp)

#     cv2.imwrite("lbp_image.png", lbp)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 002.jfif",0)

# if img is None:
#     print("Image not found!")
# else:
#     height, width = img.shape
#     lbp = np.zeros((height, width), dtype=np.uint8)

#     neighbors = [
#         (-1, -1), (-1, 0), (-1, 1),
#         (0, 1), (1, 1), (1, 0),
#         (1, -1), (0, -1)
#     ]

#     for i in range(1, height - 1):
#         for j in range(1, width - 1):

#             center = img[i, j]
#             value = 0

#             for bit, (dx, dy) in enumerate(neighbors):
#                 if img[i + dx, j + dy] >= center:
#                     value |= 1 << (7 - bit)

#             lbp[i, j] = value

#     histogram = np.bincount(
#         lbp[1:-1, 1:-1].ravel(),
#         minlength=256
#     )

#     print("Total Histogram Bins:", len(histogram))
#     print("Count of LBP Value 0:", histogram[0])
#     print("Count of LBP Value 255:", histogram[255])

#     print("Histogram:", histogram)

#     cv2.imshow("LBP Image", lbp)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
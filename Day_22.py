# All About Image Sharpening and Compressing ..

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 001.jfif")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# kernel = np.array([
#     [0, -1, 0],
#     [-1, 5, -1],
#     [0, -1, 0]
# ])
# sharp = cv2.filter2D(img, -1, kernel)
# plt.subplot(1, 2, 1)
# plt.imshow(img)
# plt.title("Original")
# plt.axis("off")

# plt.subplot(1, 2, 2)
# plt.imshow(sharp)
# plt.title("Sharpened")
# plt.axis("off")
# plt.show()



# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\sss.tif")
# img = cv2.resize(img,(300,300))
# hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
# h,s,v = cv2.split(hsv)
# kernel = np.array([
#     [0, -1, 0],
#     [-1, 5, -1],
#     [0, -1, 0]
# ])

# sharp_v = cv2.filter2D(v, -1, kernel)
# result = cv2.merge([h, s, sharp_v])
# result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Sharpened Image", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# import cv2
# import os
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\sss.tif")
# cv2.imwrite(
#     "compressed.jpg",
#     img,
#     [cv2.IMWRITE_JPEG_QUALITY, 30]
# )
# original = os.path.getsize("C:\\Users\\Officer Danyal\\Pictures\\sss.tif")
# compressed = os.path.getsize("compressed.jpg")
# saved = (original - compressed) / original * 100
# print("Original Size:", original, "bytes")
# print("Compressed Size:", compressed, "bytes")
# print("Storage Saved:", round(saved, 2), "%")

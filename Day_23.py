# All About Histogram Oriented Gradient ..


# import numpy as np
# Gx = np.array([3,5,8,11])
# Gy=np.array([4,12,6,8])
# magnitude = np.sqrt(Gx**2 + Gy**2)
# orientation = np.degrees(np.arctan2(Gy,Gx))
# print("Gradient Magnitude : ",magnitude)
# print("Oriented Magnitude : ",orientation)


# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\images (3).jfif")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.resize(gray, (64, 128))
# hog = cv2.HOGDescriptor(
#         (64, 128),  # Window size
#         (16, 16),   # Block size
#         (8, 8),     # Block stride
#         (8, 8),     # Cell size
#         9           # Orientation bins
#     )
# features = hog.compute(gray)
# print("Feature Vector Shape:", features.shape)
# print("Total Features:", len(features))
# print("First 10 Features:", features[:10].flatten())




# import numpy as np
# image1 = np.array([2, 4, 6, 8, 10])
# image2 = np.array([3, 4, 7, 8, 11])
# distance = np.sqrt(np.sum((image1 - image2) ** 2))
# print("Image 1 Features:", image1)
# print("Image 2 Features:", image2)
# print("Euclidean Distance:", distance)
# if distance < 3:
#     print("The feature vectors are similar.")
# else:
#     print("The feature vectors are different.")

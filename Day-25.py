# ALL ABOUT IMAGE SEGMENTATION....

# import cv2
# import matplotlib.pyplot as plt
# img = cv2.imread(r"C:\Users\Officer Danyal\Pictures\images (2).jfif", 0)
# ret, segmented = cv2.threshold(
#     img, 127, 255, cv2.THRESH_BINARY
# )
# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title("Original Image")
# plt.subplot(1, 2, 2)
# plt.imshow(segmented, cmap='gray')
# plt.title("Segmented Image")
# plt.show()


#
# import numpy as np
# import matplotlib.pyplot as plt

# # Create a label map
# segmentation = np.zeros((200, 300), dtype=np.uint8)

# # Class 1: Road
# segmentation[100:200, :] = 1

# # Class 2: Cars
# segmentation[120:160, 30:100] = 2
# segmentation[130:170, 150:230] = 2

# # Class 3: People
# segmentation[60:120, 250:270] = 3

# # Display segmentation
# plt.imshow(segmentation, cmap='viridis')
# plt.title("Semantic Segmentation")
# plt.colorbar()
# plt.show()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Create a binary image
# img = np.zeros((200, 300), dtype=np.uint8)

# # Draw three separate objects
# cv2.rectangle(img, (20, 50), (80, 120), 255, -1)
# cv2.rectangle(img, (110, 50), (170, 120), 255, -1)
# cv2.rectangle(img, (200, 50), (260, 120), 255, -1)

# # Find individual connected objects
# num_labels, labels = cv2.connectedComponents(img)

# # Display result
# plt.imshow(labels, cmap='nipy_spectral')
# plt.title("Instance Segmentation")
# plt.colorbar()
# plt.show()

# print("Number of objects:", num_labels - 1)



# import numpy as np
# import matplotlib.pyplot as plt

# # Create semantic segmentation map
# semantic = np.zeros((200, 300), dtype=np.uint8)

# # Stuff classes
# semantic[100:200, :] = 1  # Road
# semantic[0:100, :] = 2    # Sky

# # Thing class
# semantic[120:160, 30:90] = 3
# semantic[120:160, 150:210] = 3

# # Create instance map
# instance = np.zeros((200, 300), dtype=np.uint8)

# instance[120:160, 30:90] = 1  # Car 1
# instance[120:160, 150:210] = 2  # Car 2

# # Create combined panoptic representation
# panoptic = semantic.astype(np.int32) * 1000 + instance

# plt.imshow(panoptic, cmap='nipy_spectral')
# plt.title("Panoptic Segmentation")
# plt.colorbar()
# plt.show()

# print("Panoptic segmentation completed.")
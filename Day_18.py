# All About Pseudo Color Image Processing .....
#  (1) : 
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 002.jfif",0)
# img = cv2.resize(img, (400, 400))
# seudo = cv2.applyColorMap(img , cv2.COLORMAP_JET)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Pseudo Coloring Image : ", seudo)
# cv2.waitKey(0)


# (2) :
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 002.jfif",0)
# img = cv2.resize(img, (400, 400))
# lut = np.zeros((256 , 1 , 3),np.uint8)
# for i in range(256):
#     if i < 85:
#         lut[i,0] = [255 , 0 , 0]
#     elif i < 170:
#         lut[i,0] = [0 , 255 , 0]
#     else:
#         lut[i,0]= [0 , 0 , 255]

# seudo = cv2.applyColorMap(img,lut)
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Pesudo Image : ", seudo)
# cv2.waitKey(0)

# (3) : 
# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 00.jfif",0)
# img = cv2.resize(img ,(300,300))
# inten = np.zeros((img.shape[0], img.shape[1],3), dtype=np.uint8)
# inten[img < 64 ]= [255 , 0 , 0]
# inten[(img >= 64) & img < 128] = [0 , 255 , 0]
# inten[(img >= 128) & (img < 192)] = [0 , 255 , 255]
# inten[(img > 192)] = [0 , 0 , 255]

# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Intensity Slicing : ", inten)
# cv2.waitKey(0)


#       (4) :
# import numpy as np
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 00.jfif",0)
# result =np.zeros((img.shape[0], img.shape[1],3), dtype=np.uint8)
# result[(img >  100) & (img <=150)] = [0 , 0 , 0]
# cv2.imshow("Orignal Image : ", img)
# cv2.imshow("Specific Intensity Image : ", result)
# cv2.waitKey(0)


#(5):
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 00.jfif", 0)
# jet = cv2.applyColorMap(img, cv2.COLORMAP_JET)
# hot = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
# cv2.imshow("Original Image", img)
# cv2.imshow("JET Color Map", jet)
# cv2.imshow("HOT Color Map", hot)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#(6) :

# import cv2
# import numpy as np
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\download 00.jfif", 0)
# result = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# result[(img >= 100) & (img <= 180)] = [0, 255, 255]
# cv2.imshow("Original Image", img)
# cv2.imshow("Intensity Slicing", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
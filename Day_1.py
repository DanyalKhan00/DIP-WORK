# (1) : ...........
# import pandas as pd
# import matplotlib.pyplot as plt
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Pictures\\gg.jpg")
# img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# df = pd.DataFrame(img)
# print(df)
# #print("Image Shape : " ,img.shape);
# #print("Image Size :  ", img.size);
# plt.title("Person")
# plt.axis('off');
# plt.show()

#(2): .................
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Desktop\\download.jfif")
# print(img.shape)
# height =img.shape[0]
# print("Height : ", height)
# Weight =img.shape[1]
# print("Weight : ",Weight)
# channel =img.shape[2]
# print("Channel : ",channel)
# cv2.imshow("window",img)
# cv2.waitKey(0)

#(3): ...............

# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Desktop\\download.jfif")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("window",img)
# cv2.imshow("window",gray)
# cv2.waitKey(0)


#(4): .............................
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Desktop\\download.jfif")
# res = cv2.resize(img,(500,400))
# crp = img[100:300,150:450]
# cv2.imshow("Orignal: " , img)
# cv2.imshow("Resize : " , res)
# cv2.imshow("Crop : " , crp)
# cv2.imshow("window",img)
# cv2.waitKey(0)


#(5):.............................
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Desktop\\download.jfif")
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray ,(5,5), 0 )
# edges = cv2.Canny(blur, 50, 150)
# cv2.imshow("Original", img)
# cv2.imshow("Grayscale", gray)
# cv2.imshow("Blurred", blur)
# cv2.imshow("Edges", edges)
# cv2.waitKey(0)

#(6): ........................
# import cv2
# img = cv2.imread("C:\\Users\\Officer Danyal\\Desktop\\download.jfif")
# result = cv2.convertScaleAbs(img,alpha=1.5,beta=50)
# cv2.imshow("Original Image", img)
# cv2.imshow("Enhanced Image", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

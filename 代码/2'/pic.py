import numpy as np
import cv2
import os
import pandas as pd
import cv2
import numpy as np
img = cv2.imread(r'C:\Users\ASUS\Desktop\2021MCM_ProblemC_Files\ATT1_DSCN9647.jpg')
fdata=pd.read_excel(r"C:/Users/ASUS/Desktop/代码/美赛/C题/代码/2'/ffdata.xlsx")

fdata["R"] = fdata.apply(lambda _: 0, axis=1)
fdata["G"] = fdata.apply(lambda _: 0, axis=1)
fdata["B"] = fdata.apply(lambda _: 0, axis=1)
"""
fdata['ambigious']= fdata.apply(lambda _: 0, axis=1)
"""
cdata=pd.read_excel(r'C:\Users\ASUS\Desktop\代码\美赛\C题\2021_MCM_Problem_C_Data\2021_MCM_Problem_C_Data\2021MCM_ProblemC_ Images_by_GlobalID.xlsx')
""""

print(imageVar)
"""
cdata=cdata.set_index(["FileName"])
fdata=fdata.set_index(["GlobalID"])
path = r'C:\Users\ASUS\Desktop\2021MCM_ProblemC_Files'
file_names = os.listdir(path)
"""
for file_name in file_names:
    ID=cdata.loc[file_name,'GlobalID']
    img = cv2.imread(os.path.join(path, file_name), 1)
"""
"""
    grayVar = cv2.Laplacian(img, cv2.CV_64F).var()
    fdata.loc[ID,'ambigious']=grayVar
    print(grayVar)
"""
##cutoff of pic ,get RGBvalues
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
# subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
# blur and threshold the image
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))
# draw a bounding box arounded the detected barcode and display the image
cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", img)
cv2.imwrite("contoursImage2.jpg", img)
#cv2.waitKey(0)
Xs = [i[0] for i in box]
Ys = [i[1] for i in box]
x1 = min(Xs)
x2 = max(Xs)
y1 = min(Ys)
y2 = max(Ys)
hight = y2 - y1
width = x2 - x1
cropImg = img[y1:y1+hight, x1:x1+width]
RGBb=np.mean(cropImg[:, :, 0])
RGBg=np.mean(cropImg[:, :, 1])
RGBr=np.mean(cropImg[:, :, 2])
print(RGBb,RGBg,RGBr)
"""
fdata.loc[ID,'R']=RGBr
fdata.loc[ID, 'G'] = RGBg
fdata.loc[ID, 'B'] = RGBb
"""
#fdata.to_excel('ffdata.xlsx')

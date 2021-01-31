import numpy as np
import os
import math
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix,greycoprops
import pandas as pd
import cv2
from skimage.measure import label,regionprops
import skimage


slices=[]
proList = ['contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy']
featlist = ['sumValue','contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy','hue','value', 'saturaton','path','label']
properties =np.zeros(6)
glcmMatrix = []
final=[]
crop = "potato"
folders = ["Potato___Early_blight","Potato___healthy","Potato___Late_blight"]
# folders = ["blight","rust","mildew"]
for folder in folders:
    print(folder)
    labell=folders.index(folder)
    print(labell)
    #INPUT_SCAN_FOLDER=folder
    INPUT_SCAN_FOLDER="C:/Users/Sarita/Documents/next/"+crop+"/"+folder+"/"

    image_folder_list = os.listdir(INPUT_SCAN_FOLDER)

    for i in range(len(image_folder_list)):

        abc =cv2.imread(INPUT_SCAN_FOLDER+image_folder_list[i])

        #blur1 = cv2.GaussianBlur(abc,(51,51),1)
        
        dim = (32, 32)
        resized = cv2.resize(abc, dim, interpolation = cv2.INTER_AREA)
        #print('Resized Dimensions : ',resized.shape)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
        

        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)



        
        lower_red = np.array([5,50,50])
        upper_red  = np.array([20,255,255])
        mask = cv2.inRange(hsv,lower_red,upper_red)
        res = cv2.bitwise_and(resized,resized,mask=mask)
        plt.imshow(res,cmap='Blues', interpolation = 'bicubic')
        plt.xticks([]),plt.yticks([])
        #plt.show()"""


        """gray_image = cv2.cvtColor(abc, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(abc, cv2.COLOR_BGR2HSV)



        
        lower_red = np.array([10,50,50])
        upper_red  = np.array([20,255,255])
        mask = cv2.inRange(hsv,lower_red,upper_red)
        res = cv2.bitwise_and(abc,abc,mask=mask)
        plt.imshow(res,cmap='Blues', interpolation = 'bicubic')
        plt.xticks([]),plt.yticks([])
        #plt.show()"""

        
        sum=0
        result=res.flatten()
        #print(len(result))
        for k in range(3072):
            sum+=result[k]^2
        #print(sum)
        sqsum=math.sqrt(sum)
        #print(sqsum)

        
        
        h,s,v = cv2.split(hsv)
        h_mean = np.mean(h)
        h_mean = np.mean(h_mean)

        s_mean = np.mean(s)
        s_mean = np.mean(s_mean)

        v_mean = np.mean(v)
        v_mean = np.mean(v_mean)


       


        glcmMatrix = (greycomatrix(gray_image, [1], [0], levels=2 ** 8))
        
        
        for j in range(0, len(proList)):
            properties[j] = (greycoprops(glcmMatrix, prop=proList[j]))

        #print("properties are:")
        #print(properties)

        features =np.array([sqsum,properties[0], properties[1], properties[2], properties[3], properties[4],h_mean,s_mean,v_mean,INPUT_SCAN_FOLDER+image_folder_list[i],labell])
        final.append(features)
#print(len(final))

df = pd.DataFrame(final, columns=featlist)
df.to_csv("glfeat.csv")
s=pd.read_csv("glfeat.csv")
for i in s.iterrows():
#t=s['label']
    print(i)
#print(s)"""


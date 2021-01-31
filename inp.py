from PIL import Image
import numpy as np
import cv2
import csv
import math
#import ui
from matplotlib import pyplot as plt
import sys
import os


from skimage.feature import greycomatrix,greycoprops
import pandas as pd
from skimage.measure import label,regionprops
import skimage

def loadDataset(filename, trainingSet=[] ,trainingClass=[]):
    arr=[]
    names = ['sumValue','contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy','hue','value', 'saturaton','path','label']
    dataset = pd.read_csv(filename,names=names)
    X = dataset.iloc[:, :-2].values
    y = dataset.iloc[:, 10].values
    for i in range(1,len(dataset)):
        trainingSet.append(X[i])
        trainingClass.append(y[i])
    print(len(X))



def feature_extract(im,features=[]):
    slices=[]
    proList = ['contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy']
    #featlist = ['sumValue','contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy','hue', 'saturaton','value']
    properties =np.zeros(6)
    glcmMatrix = []
    

    img=cv2.imread(im,1)
    #print('Original Dimensions : ',img.shape)
    dim = (32, 32)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    #print('Resized Dimensions : ',resized.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([10,50,50])
    upper_red  = np.array([20,255,255])
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(resized,resized,mask=mask)
    plt.imshow(res,cmap='Blues', interpolation = 'bicubic')
    plt.xticks([]),plt.yticks([])
    #plt.show()

    
    sum=0
    result=res.flatten()
    #print(len(result))
    for k in range(3072):
        sum+=result[k]^2
    #print(sum)
    sqsum=math.sqrt(sum)
    print(sqsum)
    features.append(sqsum)


    
    h,s,v = cv2.split(hsv)
    h_mean = np.mean(h)
    h_mean = np.mean(h_mean)

    s_mean = np.mean(s)
    s_mean = np.mean(s_mean)

    v_mean = np.mean(v)
    v_mean = np.mean(v_mean)


       


    glcmMatrix = (greycomatrix(gray_image, [1], [0], levels=2 ** 8))
    #print(glcmMatrix)
        
        
    for j in range(0, len(proList)):
        properties[j] = (greycoprops(glcmMatrix, prop=proList[j]))
        features.append(properties[j])

    features.append(h_mean)
    features.append(s_mean)
    features.append(v_mean)
    #features=np.asarray(features)
    #features =[sqsum,properties[0], properties[1], properties[2], properties[3], properties[4],h_mean,s_mean,v_mean]
    #print(features)
    #print(properties)"""
    
    






def knn(trainingSet ,trainingClass,features,k):
    
    row3=[]
    row2=[]
    row1=[]
    for training_instance,train_instance in zip(trainingSet,trainingClass):
        distance=pow((float(features[0]) - float(training_instance[0])), 2)
        dist=math.sqrt(distance)
        row_dict={'class':train_instance,'value':dist}
        row1.append(row_dict)
    #print(len(row1))
    row2=sorted(row1, key = lambda i: i['value'])
    #print(len(row2))
        
    for i in range(k):
        row3.append(row2[i])
    test_array=np.asarray(row3)
    #print(test_array)
    
    healthy_count=0
    unhealthy_count=0
    for j in test_array:
        if(j.get('class')=='1'):
            healthy_count+=1
        else:
            unhealthy_count+=1
            #late_count+=1

    print("The data for test data %s is: "%j.get('name'))
    print("Healthy=",healthy_count)
    print("Unhealthy=",unhealthy_count)    
        
    if(healthy_count >= unhealthy_count):
        diagno="Leaf is Healthy"
    else:
        row3=[]
        row2=[]
        row1=[]
        for training_instance,train_instance in zip(trainingSet,trainingClass):
            distance=0
            for x in range(1,9):
                #print(tes_instance[x])
                distance += pow((float(features[x]) - float(training_instance[x])), 2)
            dist=math.sqrt(distance)
            row_dict={'class':train_instance,'value':dist}
            row1.append(row_dict)
        row2=sorted(row1, key = lambda i: i['value'])
        
        for i in range(k):
            row3.append(row2[i])

        test_array=np.asarray(row3)
        #print(test_array)
    
        early_count=0
        late_count=0
        healthy_count=0
        for j in test_array:
            if(j.get('class')=='0'):
                early_count+=1
            elif(j.get('class')=='1'):
                healthy_count+=1
            elif(j.get('class')=='2'):
                late_count+=1

        print("The data for test data %s is: "%j.get('name'))
        print("Early_Blight=",early_count)
        print("Late_Blight=",late_count)
        print("Healthy=",healthy_count)
        
        
        if(early_count >= late_count):
            diagno="Leaf is suffered from Early_Blight"
        else:
            diagno="Leaf is suffered from Late_Blight"
    return diagno
    os.remove('resized.jpg')








    


def main():
    features=[]
    trainingSet=[];
    trainingClass=[];
    training_file = 'glfeat.csv'
    loadDataset(training_file,trainingSet,trainingClass)
    #print(trainingSet)
    #print(len(trainingSet))
   
    k = 300

    im = "resized.jpg"
    #im =input("Enter an image")

     

        #if not training_set:
            #print('Empty training set')

    if not im:
        print("no input image")

    elif k > len(trainingSet):
        print('Expected number of neighbors is higher than number of training data instances')

    else:
        feature_extract(im,features)
        print(features)
        diagno=knn(trainingSet,trainingClass,features,k)

        print(diagno)
        return diagno
    """except ValueError as v:
            print(v)

        except FileNotFoundError:
            print('File not found')
        #print("hello")
        #print(st)
        #return st"""
  

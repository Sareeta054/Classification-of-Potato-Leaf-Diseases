from sys import exit
from math import sqrt
from operator import itemgetter
from PIL import Image
import numpy as np
import cv2
import csv
import math
import pandas as pd
import random
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

def knn(k,trainingSet , testSet,trainingClass,testClass):
    test_data=[[]]
    for test_instance,tes_instance in zip(testSet,testClass):
        row3=[]
        row2=[]
        row1=[]
        for training_instance,train_instance in zip(trainingSet,trainingClass):
            distance=0
            for x in range(9):
               
                distance += pow((float(test_instance[x]) - float(training_instance[x])), 2)
            dist=math.sqrt(distance)
            row_dict={'predicted_class':train_instance,'actual_class':tes_instance,'value':dist}
            row1.append(row_dict)
        row2=sorted(row1, key = lambda i: i['value'])
        
        for i in range(k):
            row3.append(row2[i])
        test_data.append(row3)

    list2 = [e for e in test_data if e]
    test_array=np.asarray(list2)
    actual=[]
    predicted=[]
    
    for i in test_array:
        early_count=0
        healthy_count=0
        late_count=0
        for j in i:
            if(j.get('predicted_class')=='0'):
                early_count+=1
            elif(j.get('predicted_class')=='1'):
                healthy_count+=1
            elif(j.get('predicted_class')=='2'):
                late_count+=1
            count+=1
    
        """print("The data for test data %s is: "%j.get('name'))
        print("Early_Blight=",early_count)
        print("Healthy=",healthy_count)
        print("Late_Blight=",late_count)"""
    

        if(healthy_count >= max(early_count,late_count)):
            predicted.append('1')
            actual.append(j.get('actual_class'))
        elif(early_count >= max(healthy_count,late_count)):
            predicted.append('0')
            actual.append(j.get('actual_class'))
        else:
            predicted.append('2')
            actual.append(j.get('actual_class'))
    

    print(predicted)
    print(actual)
    results = confusion_matrix(actual, predicted)
    print('Confusion Matrix :')
    print(results) 
    print('Accuracy Score :',accuracy_score(actual, predicted))
    print('Report : ')
    print(classification_report(actual, predicted))
        
        
        
        


def loadDataset(filename, split, trainingSet=[] , testSet=[],trainingClass=[],testClass=[]):
    arr=[]
    names = ['sumValue','contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy','hue', 'saturaton','value','path','label']
    dataset = pd.read_csv(filename,names=names)
    X = dataset.iloc[:, :-2].values
    y = dataset.iloc[:, 10].values
    
    for x in range(1,len(dataset)-1):
        if random.random() <= split:
            trainingSet.append(X[x])
            trainingClass.append(y[x])
        else:
            testSet.append(X[x])
            testClass.append(y[x])


    print(len(trainingSet))
    print(len(testSet))
    

    


testClass=[]
trainingClass=[]
trainingSet=[]
testSet=[]
loadDataset('glfeat.csv', 0.66, trainingSet, testSet,trainingClass,testClass)
knn(300,trainingSet, testSet,trainingClass,testClass)

    

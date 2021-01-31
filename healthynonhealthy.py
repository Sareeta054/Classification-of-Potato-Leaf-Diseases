import pandas as pd
import math
import csv
from sklearn import preprocessing
import random
import numpy as np

from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 


def knn(k,trainingSet , testSet,trainingClass,testClass,actual=[],predicted=[]):
    for test_instance,tes_instance in zip(testSet,testClass):
        row3=[]
        row2=[]
        row1=[]
        for training_instance,train_instance in zip(trainingSet,trainingClass):
            #dist = abs(float(test_instance[0]) - float(training_instance[0]))
            distance=pow((float(test_instance[0]) - float(training_instance[0])), 2)
            dist=math.sqrt(distance)
            if(tes_instance=='2'):
               tes_instance='0';
            row_dict={'predicted_class':train_instance,'actual_class':tes_instance,'value':dist}
            row1.append(row_dict)
               
        row2=sorted(row1, key = lambda i: i['value'])
        
        for i in range(k):
            row3.append(row2[i])
        test_array=np.asarray(row3)

        healthy_count=0
        unhealthy_count=0
        for j in test_array:
            
            if(j.get('predicted_class')=='1'):
                healthy_count+=1
            else:
                unhealthy_count+=1
                
        if(healthy_count >= unhealthy_count):
            predicted.append('1')
            actual.append(j.get('actual_class'))
        else:
            predicted.append('0')
            actual.append(j.get('actual_class'))
            
            
    results = confusion_matrix(actual, predicted) 
    print('Confusion Matrix :')
    print(results) 
    print('Accuracy Score :',accuracy_score(actual, predicted))
    print('Report : ')
    print(classification_report(actual, predicted))
    

    

    



def loadDataset(filename, split, trainingSet=[] , testSet=[], trainingClass=[],testClass=[]):
    arr=[]
    names = ['sumValue','contrast', 'dissimilarity', 'homogeneity', 'ASM', 'energy','hue','value', 'saturaton','path','label']
    dataset = pd.read_csv(filename,names=names)
    X = dataset.iloc[:, :-2].values
    y = dataset.iloc[:, 10].values

    #print(len(dataset))
    
    for x in range(1,len(dataset)):
        if random.random() <= split:
            trainingSet.append(X[x])
            trainingClass.append(y[x])
        else:
            testSet.append(X[x])
            testClass.append(y[x])


    #print(len(trainingSet))
    #print(len(testSet))



    
    
    

actual=[]
predicted=[]

testClass=[]
trainingClass=[]
trainingSet=[]
testSet=[]
loadDataset('glfeat.csv', 0.66, trainingSet, testSet,trainingClass,testClass)
knn(700,trainingSet, testSet,trainingClass,testClass,actual,predicted)


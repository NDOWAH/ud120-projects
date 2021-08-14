#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time
from sklearm.svm import SVC
sys.path.append("../tools/")
from email_preprocess import preprocess



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
clf = SVC(c=1.0,kernel="linear",gamm="auto")
clf.fit(feature_train,feature_test)



#########################################################
### your code goes here ###
from sklearn.metrics import accuracy_score
pred = clf.predict(label_test)
acc = accuracy_score(pred, labels_test)

def submitAccuracy():
    return acc
#########################################################



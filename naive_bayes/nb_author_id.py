#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
<<<<<<< HEAD
from sklearn.naive_bayes import GaussianNB
from sklearn.matrics import accuracy_score
def naive_bayes_classifier(features):
    clf= GaussianNB()
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    accuracy = accuracy_score(features_test, labels_test)
    return pred, accuracy


||||||| 9ee2a2e

=======
from sklearn.naive_bayes import GaussianNB
from sklearn.matrics import accuracy_score
def naive_bayes_classifier(features):
    cls = GaussianNB()
    cls.fit(feature_train, label_train)
    pred = prediction(feature_test)
    accuracy = accuracy_score(feature_test, label_test)
    return pred, accuracy
>>>>>>> 391b41c030416c3bfb4e5db44bffb1751e8133ff

#########################################################


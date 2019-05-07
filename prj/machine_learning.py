#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:42:58 2019

@author: gayathri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset =  pd.read_csv('/home/gayathri/project/MakeComplaint/data.csv')

x = dataset.iloc[:,1:-1]
y = dataset.iloc[:,3].values

dataset['Subject'] = dataset['Subject'] =dataset['Subject'].str.replace('[^\w\s]','').str.lower()
dataset['Complaint'] = dataset['Complaint'].str.replace(',',' ').str.lower() 
dataset['Subject'] =  dataset['Subject'] .str.replace('\d+', ' ')
dataset['Complaint'] =  dataset['Complaint'] .str.replace('\d+', ' ')
dataset['Subject'] = dataset['Subject'].str.rstrip('\n')

dataset['Subject_and_Complaint'] = dataset['Subject'] + " " + dataset['Complaint']
        
x = dataset.iloc[:,4].values

#splitting the data

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.2,random_state = 0)

#Categorical data processing
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)

label_encoder_x = LabelEncoder()
x = label_encoder_y.fit_transform(x)


'''#Encoding the complaint data
import skipthoughts

class SkipThoughtsVectorizer(object):
    def __init__(self):

        self.model = skipthoughts.load_model()
        self.encoder = skipthoughts.Encoder(self.model)

    def fit_transform(self, raw_documents, y):
    	return self.encoder.encode(raw_documents, verbose=False)
    
    def fit(self, raw_documents, y=None):
    	self.fit_transform(raw_documents, y)
    	return self

    def transform(self, raw_documents, copy=True):
    	return self.fit_transform(raw_documents, None)

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

pipeline_skipthought = Pipeline(steps=[('vectorizer', SkipThoughtsVectorizer()),
                        ('classifier', LogisticRegression())])
                     

pipeline_tfidf = Pipeline(steps=[('vectorizer', TfidfVectorizer(ngram_range=(1, 2))),
                        ('classifier', LogisticRegression())])
feature_union = ('feature_union', FeatureUnion([
    ('skipthought', SkipThoughtsVectorizer()),
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
]))



pipeline_both = Pipeline(steps=[feature_union,
                        ('classifier', LogisticRegression())])

# Train and test the models
for train_size in (10,20,30,40,50,60, len(x_train)):
    print(train_size, '--------------------------------------')
    # skipthought
    pipeline_skipthought.fit(x_train[:train_size], classes_train[:train_size])
    print ('skipthought', pipeline_skipthought.score(x_test, y_test))

    # tfidf
    pipeline_tfidf.fit(x_train[:train_size], classes_train[:train_size])
    print('tfidf', pipeline_tfidf.score(x_test, y_test))

    # both
    pipeline_both.fit(tweets_train[:train_size], classes_train[:train_size])
    print('skipthought+tfidf', pipeline_both.score(x_test, y_test))'''
    




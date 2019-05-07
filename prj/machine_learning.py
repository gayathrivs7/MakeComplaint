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
#Encoding the complaint data
import gensim
from gensim.models import Word2Vec


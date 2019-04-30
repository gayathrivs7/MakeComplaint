#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:27:15 2019

@author: gayathri
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

dataset = pd.read_csv('/home/gayathri/Documents/Data_Preprocessing/ml.csv',encoding = 'utf8')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values


imputer  = SimpleImputer(missing_values = np.nan,strategy='mean',fill_value = None,verbose = 0,copy = True )
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#categorical data
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()

label_encode_y = LabelEncoder()
y = label_encode_y.fit_transform(y)

#splitting dataset into train and test 

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.2,random_state = 0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test  = sc_x.transform(x_test)






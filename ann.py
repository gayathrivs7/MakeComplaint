#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:49:22 2019

@author: gayathri
"""
#Ann
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('/home/gayathri/Documents/Machine Learning A-Z Template Folder/Part 8 - Deep Learning/Section 39 - Artificial Neural Networks (ANN)/Artificial_Neural_Networks/Churn_Modelling.csv')

x = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values

#categorical  data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_encoder = LabelEncoder()
x[:,1]    = label_encoder.fit_transform(x[:,1])
onehotencoder = OneHotEncoder(categorical_features = [1,2])
x             = onehotencoder.fit_transform(x).toarray()



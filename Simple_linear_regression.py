#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:11:57 2019

@author: gayathri
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset =  pd.read_csv('/home/gayathri/Documents/Machine Learning A-Z Template Folder/Part 2 - Regression/Section 4 - Simple Linear Regression/Salary_Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#Predicting  the test results
y_predict = regressor.predict(x_test)

#visualising the training set results
plt.scatter(x_train,y_train,color='red')
plt.scatter(x_train,regressor.predict(x_train))
plt.title('Training set results')
plt.show()
plt.scatter(x_test,y_test,color='red')
plt.scatter(x_train,regressor.predict(x_train),color='blue')
plt.title('Test set results')
plt.show()







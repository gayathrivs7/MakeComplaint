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

x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,3].values


#Categorical data processing
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

label_encoder_y = LabelEncoder()
y = label_encoder_y.fit_transform(y)



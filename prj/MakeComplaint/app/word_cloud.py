#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:47:48 2019

@author: gayathri
"""

# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt


# Load in the dataframe
df = pd.read_csv("/home/gayathri/project/MakeComplaint/train.csv")


# Groupby by Department
department= df.groupby("Departments")


# Summary statistic of all countries
department.describe().head()

print("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

print("There are {} types of departments in this dataset such as {}... \n".format(len(df.Departments.unique()),
                                                                           ", ".join(df.Departments.unique()[0:5])))
df[["Subject", "Complaint","Departments"]].head()


plt.figure(figsize=(15,10))

department.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Departments")
plt.ylabel("Complaints")
plt.show()
?WordCloud

water = df.loc[df['Departments'] == 'Water Authority']
pwd = df.loc[df['Departments'] == 'PWD']
ksrtc = df.loc[df['Departments'] == 'KSRTC']
kseb = df.loc[df['Departments'] == 'KSEB']
env = df.loc[df['Departments'] == 'Environment and climate change']

df_water = water[['Subject','Complaint']]
df_pwd   = pwd[['Subject','Complaint']]
df_ksrtc = ksrtc[['Subject','Complaint']]
df_kseb  = kseb[['Subject','Complaint']]
df_env   = env[['Subject','Complaint']]
dataset = df[["Subject", "Complaint"]]

dfwater  = df_water[['Subject','Complaint']]
dfpwd    = df_pwd[['Subject','Complaint']]
dfksrtc  = df_ksrtc[['Subject','Complaint']]
dfkseb   = df_kseb[['Subject','Complaint']]
dfenv    = df_env[['Subject','Complaint']]


dfwater['Subject_and_Complaint'] = df_water['Subject'] + " "+ df_water['Complaint']
dfwater=dfwater[['Subject_and_Complaint']]

#Dataframe with complaint and subject as one column = PWD
dfpwd['Subject_and_Complaint'] = df_pwd['Subject'] + " "+ df_pwd['Complaint']
dfpwd=dfpwd[['Subject_and_Complaint']]
#print(dfpwd)

#Dataframe with complaint and subject as one column = ksrtc
dfksrtc['Subject_and_Complaint'] = df_ksrtc['Subject'] + " "+ df_ksrtc['Complaint']
dfksrtc=dfksrtc[['Subject_and_Complaint']]
#print(dfksrtc)

#Dataframe with complaint and subject as one column = kseb
dfkseb['Subject_and_Complaint'] = df_kseb['Subject'] + " "+ df_kseb['Complaint']
dfkseb=dfkseb[['Subject_and_Complaint']]
#print(dfkseb)


#Dataframe with complaint and subject as one column = env
dfenv ['Subject_and_Complaint'] = df_env['Subject'] + " "+ df_env['Complaint']
dfenv =dfenv [['Subject_and_Complaint']]
print(dfenv )



import spacy
nlp = spacy.load('en_core_web_md')



def string_format (df):
    

    text_list= []
    for i, row in df.iterrows():
        df_row  =  nlp(row['Subject_and_Complaint'])
        for word in df_row:
            text_list.append(word.text)
    #print(text_list)
            
    water= "is"  
    # Create and generate a word cloud image:
    for i in text_list:
        water= water+" "+i
        
    #print(water)


    
    wordcloud = WordCloud(max_font_size=40, background_color="white",contour_color="black",contour_width=5,mode="RGBA").generate(water)
    
    # Display the generated image:
    plt.figure(figsize=(8,3))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


string_format(dfwater)
string_format(dfpwd)
string_format(dfenv)
string_format(dfkseb)
string_format(dfksrtc)

#=====================================================================================================


water_mask = np.array(Image.open("/home/gayathri/project/MakeComplaint/prj/water2.png"))
water_mask







def transform_format(val):
    if val == 0:
        return 255
    else:
        return val


# Transform your mask into a new one that will work with the function:

transformed_water_mask = np.ndarray((water_mask.shape[0],water_mask.shape[1]), np.int32)

for i in range(len(water_mask)):
    transformed_water_mask[i] = list(map(transform_format, water_mask[i]))
transformed_water_mask

# Create a word cloud image
wc = WordCloud(background_color="white", max_words=1000, mask=transformed_water_mask,
               stopwords=stopwords, contour_width=3, contour_color='firebrick')














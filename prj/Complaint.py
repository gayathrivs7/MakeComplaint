#main program
import spacy
import pandas as pd
import preprocess
from preprocess import data_clean #preprocess.py
import dataframes
from dataframes import dataframing
import tokenise
from tokenise import tokenisation
import frequency
from frequency import word_frequency
import topwords
from topwords import most_repeated_keywords
import testdata
from testdata import test
import department
from department import department_class
import predict
from predict import evaluate





class Complaint:
    
    

    def __init__(self,dataset,nlp):
        #/home/gayathri/project/MakeComplaint/data.csv
        self.dataset=dataset

        #print(self.dataset)
        self.dataset= pd.read_csv(self.dataset)
        self.nlp =nlp

     #department headings class names.
    def department_class(self):
        datasets=self.dataset
        departments=self.dataset['Departments'].unique()
        return departments,datasets


 #Execution begins
files =   '/home/gayathri/project/MakeComplaint/data.csv'   
#nlp = spacy.load('en_core_web_md')
         
#c = Complaint(files,nlp)

#category,dataset = c.department_class()

#dataset = preprocess.data_clean(dataset)

#dfwater,dfpwd,dfksrtc,dfkseb,dfenv = dataframes.dataframing(dataset)

#water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm = tokenise.tokenisation(dfwater,dfpwd,dfksrtc,dfkseb,dfenv)

#water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq = frequency.word_frequency(water_lemm,pwd_lemm,ksrtc_lemm,kseb_lemm,env_lemm)


#water_lis,pwd_lis,ksrtc_lis,kseb_lis,env_lis=topwords.most_repeated_keywords(dfwater,dfpwd,dfksrtc,dfkseb,dfenv,water_freq,pwd_freq,ksrtc_freq,kseb_freq,env_freq,"manual")
#no need                dept=department_class()
#keywords,item=testdata.test()
#predict.evaluate(keywords,item,water_lis,env_lis,pwd_lis,ksrtc_lis,kseb_lis,category,nlp)
#main program
import spacy
import pandas as pd
import preprocess
from preprocess import data_clean #preprocess.py
import dataframes
from dataframes import dataframing



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
file =   '/home/gayathri/project/MakeComplaint/data.csv'   
nlp = spacy.load('en_core_web_md')
         
c = Complaint(file,nlp)

category,dataset = c.department_class()

dataset = preprocess.data_clean(dataset)

dfwater,dfpwd,dfksrtc,dfkseb,dfenv = dataframes.dataframing(dataset)

    


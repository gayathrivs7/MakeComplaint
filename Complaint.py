#main program
import spacy
import pandas as pd
from preprocess import data_clean #preprocess.py
import preprocess



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
preprocess.data_clean(dataset)

    


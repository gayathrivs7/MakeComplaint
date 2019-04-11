#main program
import spacy
import pandas as pd

class Complaint:

    

    def __init__(self,dataset,nlp):
        #/home/gayathri/project/MakeComplaint/data.csv
        self.dataset=dataset
        #print(self.dataset)
        self.dataset= pd.read_csv(self.dataset)
        self.nlp =nlp





 #Execution begins
file =   '/home/gayathri/project/MakeComplaint/data.csv'   
nlp = spacy.load('en_core_web_md')
         
c = Complaint(file,nlp)

    


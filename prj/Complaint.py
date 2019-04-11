#main program
import init
import spacy

class Complaint:
    file =   '/home/gayathri/project/MakeComplaint/data.csv'   
    nlp = spacy.load('en_core_web_md')

    init.init(file,nlp)
    


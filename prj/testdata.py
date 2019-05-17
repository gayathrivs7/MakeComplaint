import re
from nltk.tokenize import word_tokenize 
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


def test(text_data):
    
    text_data= text_data.replace('[^\w\s]','').lower()
    porter=PorterStemmer()
    stemmer = SnowballStemmer("english")
    lemmatizer = WordNetLemmatizer()
    

    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for x in text_data.lower(): 
        if x in punctuations: 
            text_data = text_data.replace(x, " ") 


    #print(text_data) 
    
        
    test_token = word_tokenize(text_data)
    #print(test_token)
    test_list =[]

    import spacy
    spacy_nlp = spacy.load('en_core_web_sm')
    spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
   
    for i in test_token:
        
        
        if i not in spacy_stopwords:
    
            test_list.append(i)
    print("Test List")
    print(test_list)

    '''New changes'''


    

    #stemming and lemmatization 
    
    test_list





    
    #frequency : 
    
   
    #with stem and lemma
    counts = Counter(test_list)
    count = dict(counts)
    #print(count)  # word frequency



    items = [(v, k) for k, v in counts.items()]
    items.sort()
    items.reverse() 
    item = [(k,v) for v, k in items]
    count_list = [v for v,k in items]

    #print("Count list ")
    #print(count_list)
    count_list = count_list[:5]

    #print(count_list)
    prob_list = []
    for i in count_list:
        prob = i/5
        prob_list.append(prob)
    #print("\n \n Probability list")
    #print(prob_list)

    items = [k for v, k in items]
    #print(items)  # sorted high to low
    test_dict=(items[0:5])
    #print(test_dict)  #key only
    
    return(test_dict,item)

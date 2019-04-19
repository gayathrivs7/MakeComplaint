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


    print(text_data) 
    
        
    test_token = word_tokenize(text_data)
    print(test_token)
    test_list =[]
    
    stop_words = set(stopwords.words('english'))
    for i in test_token:
        
        
        if i not in stop_words:
    
            test_list.append(i)
    print(test_list)

    #stemming and lemmatization 
    test_stem = []
    for i in test_list:
        t = stemmer.stem(i)
        test_stem.append(t)

    test_lemm = []
    for i in test_list:
        t = lemmatizer.lemmatize(i)
        test_lemm.append(t)
    
    test_list = test_lemm





    
    #frequency : 
    

    
    counts = Counter(test_list)
    count = dict(counts)
    print(count)  # word frequency

    items = [(v, k) for k, v in counts.items()]
    items.sort()
    items.reverse() 
    item = [(k,v) for v, k in items]
    items = [k for v, k in items]
    print(items)  # sorted high to low
    test_dict=(items[0:5])
    print(test_dict)  #key only
    
    return(test_dict,item)

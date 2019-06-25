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
    
    text_data= text_data.replace('[^\w\s]','')
    porter=PorterStemmer()
    stemmer = SnowballStemmer("english")
    lemmatizer = WordNetLemmatizer()
    

    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for x in text_data: 
        if x in punctuations: 
            text_data = text_data.replace(x, " ") 


    #print(text_data) 
    
        
    test_token = word_tokenize(text_data)
    #print(test_token)
    test_list =[]

    import spacy
    
  
    #===============Removing Stop Words=================================
    spacy_nlp = spacy.load('en_core_web_sm')
    spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
    spacy_stopwords=list(STOP_WORDS)
    spacy_stopwords.append('kindly')
    spacy_stopwords.append('shall')
    spacy_stopwords.append('thank')
    spacy_stopwords.append('need')
    spacy_stopwords.append('time')
    spacy_stopwords.append('look')
    spacy_stopwords.append('matter')
    spacy_stopwords.append('personally')
    spacy_stopwords.append('needful')
    spacy_stopwords.append('thankful')
    spacy_stopwords.append('try')
    spacy_stopwords.append('The')
    spacy_stopwords.append('totally')
    for i in test_token:
        if i not in spacy_stopwords:
            test_list.append(i)
    print("Test List")
    print(test_list)

    #===============Removing NNP=================================
    nlp = spacy.load('en')
    nnp_list=[]

    # to make spacy.tokens.token.Token
    str =""
    for element in test_list:
        str+=" "+element
    print(str)

    str_tokens=[]
    str = nlp(str)
    for i in str:
        str_tokens.append(i.text)
        
        print(type(i))
        if i.tag_=='NNP':
            print(type(i))
            nnp_list.append(i.text)
    print("NNP List")
    print(nnp_list)
    print("Str Tokens")
    str_tokens.pop(0)
    print(str_tokens)
    
    new_testlist=[]
    if len(nnp_list)!=0:
    
        for i in str_tokens:
            for j in nnp_list:
                if i!=j:
                    new_testlist.append(i)
    print("\nNew Test List without NNP")
    print(new_testlist)
   


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

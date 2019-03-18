#using NLTK library, we can do lot of text preprocesing
import nltk
from nltk.tokenize import word_tokenize

#function to split text into word

tokens = word_tokenize("The quick brown fox jumps over the lazy dog")
#========================================================================

#correct
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))
#======================================
from nltk.tokenize import sent_tokenize, word_tokenize
data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(sent_tokenize(data))
#===========================================

 
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
 
phrases = sent_tokenize(data)
words = word_tokenize(data)
 
print(phrases)
print(words)
#==================================Stopwords removal================
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english')) 
print(stopWords)
words = word_tokenize(data)
wordsFiltered = []
for w in words:
    if w not in stopWords:
        wordsFiltered.append(w)
print(wordsFiltered)

#========================Stemming=================================

#stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
# went is not working
words = ["game","gaming","gamed","games"]
ps = PorterStemmer()

for w in words:
    print(w ," : " ,ps.stem(w))
#===============================stemming modified=====

#stemming
#3 stemmer alogirthms are used here

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer


# went is not working
words = ["go","went","gone","games"]
ps = PorterStemmer()
lanca_stemmer = LancasterStemmer()
sb_stemmer = SnowballStemmer("english",)
print("=========Porter Stemmer======")
for w in words:
    print(w ," : " ,ps.stem(w))
    
print("=========Lanca Stemmer======")
for w in words:

    print(w ," : " ,lanca_stemmer.stem(w))
    
print("=========Snowball Stemmer======")
for w in words:
    
    print(w ," : " ,sb_stemmer.stem(w))
    
    
 #Porter stemmer and Snowball stemmer working in similar manner   
#lanca is not so good
#=========================================Speech Tagging============================
# labels verbs,nouns,pronouns etc

#speech tagging

import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import PunktSentenceTokenizer

document = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'
sentences = nltk.sent_tokenize(document) 
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))

#=============Filtering from Speech tagging=================
#filtering from Speech tagging
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

document = 'Today the Netherlands celebrates King\'s Day. To honor this tradition, the Dutch embassy in San Francisco invited me to'
sentences = nltk.sent_tokenize(document)  
data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))
for w in data:
    if 'VB' in w[1]:
        print(w)

#================================================================================================
# NLP Tokenization thurdsay March 14



import nltk
#Tokenzie using TreeBank Tokenizer

text="This is Gayathri's book isn't it?"

tokenizer=nltk.tokenize.TreebankWordTokenizer()
tokenizer1=nltk.tokenize.WordPunctTokenizer()

tokens=tokenizer.tokenize(text)
tokens1=tokenizer1.tokenize(text) #wordPunct

print("Tree", tokens)
print("WordPunct" ,tokens1)
#=====================
import nltk

#

text="This is Gayathri's book isn't it?"

lemmatizer=nltk.stem.WordNetLemmatizer()

" ".join(lemmatizer.lemmatize(token)for token in tokens)
#================stemming
#stemmer
stemmer=nltk.stem.PorterStemmer()
print("porter stemmer")
" ".join(stemmer.stem(token)for token in tokens)

























import nltk
import spacy
import pandas as pd

nlp = spacy.load('en') #loading English

data=pd.read_table('/home/user/Complaint/MakeComplaint/data.csv')
frames = [data]

#opening csv
myfile = open('/home/user/Complaint/MakeComplaint/data.csv').read()
frames = [data]
doc_file= nlp(myfile)


#fetching the headers

for colname in frames:
    print(colname.columns)
    
    
    
#keys = ['Water Authority','KSEB','KSRTC','PWD','Environment and climate change','MVD']
#df=pd.concat(frames,keys=keys)
#df
print(frames)



#print(doc_file)

#tokenizer=nltk.tokenize.TreebankWordTokenizer()
#tokens=tokenizer.tokenize(text)
#print("Tree", tokens)


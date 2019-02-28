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
    print(ps.stem(w))


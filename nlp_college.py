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

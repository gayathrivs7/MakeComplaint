import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ex = 'In Sreekaryam road is not maintained Gayathri water environment.Could you please help Japan '
sent = nltk.word_tokenize(ex)
sent = nltk.pos_tag(sent)
print(sent)
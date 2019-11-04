import nltk
import pdfminer
import os
from nltk.corpus import stopwords

#open file
f = open('document.txt')
raw = f.read()

#tokening
tokens = nltk.word_tokenize(raw)

#cargar stopwords
stop_words = set(stopwords.words('english'))

#Stemming
porter = nltk.PorterStemmer()
tokens_stem = [porter.stem(t) for t in tokens ]

#Lemmatization
wnl = nltk.WordNetLemmatizer()
tokens_lem = [wnl.lemmatize(t) for t in tokens_stem]



print(tokens)

print(stop_words)
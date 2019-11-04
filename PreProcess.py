import nltk
import pdfminer
import os
from nltk.corpus import stopwords



def PreProces(text):
    #tokening
    tokens = nltk.word_tokenize(text)

    #Remove stopwords
    tokens_stopw = [x for x in tokens if x.lower() not in stop_words]

    #Stemming
    porter = nltk.PorterStemmer()
    tokens_stem = [porter.stem(t) for t in tokens_stopw ]

    #Lemmatization
    wnl = nltk.WordNetLemmatizer()
    tokens_lem = [wnl.lemmatize(t) for t in tokens_stem]

    return tokens_lem


if __name__ == '__main__':
    # open file
    f = open('/home/leandro/PycharmProjects/untitled/SI/docs/document.txt')
    raw = f.read()

    # cargar stopwords
    stop_words = set(stopwords.words('english'))

    print(PreProces(raw))
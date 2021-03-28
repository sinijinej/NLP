

path = 'YOUR TXT FILE PATH HERE'

f = open(path, "r")


data = (f.read())

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
import numpy

def sent_std(text_string):  # data should be string
    tokenizer = RegexpTokenizer(r'\w+') 
    tokenised_sent = sent_tokenize(data)


    x = [tokenizer.tokenize(x) for x in tokenised_sent]

    lengthlist = []

    for i in x:
        lengthlist.append(len(i))

    stdeviation = numpy.std(lengthlist)
    
    return stdeviation

std = sent_std(data)


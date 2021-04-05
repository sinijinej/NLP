'''
#for one file
path = 'YOUR TXT FILE PATH HERE'
f = open(path, "r")
data = (f.read())
'''

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, RegexpTokenizer
import numpy
import os
import pandas as pd





def sent_std(text_string):  # data should be string
    tokenizer = RegexpTokenizer(r'\w+') 
    
    tokenised_sent = sent_tokenize(text_string)
    x = [tokenizer.tokenize(x) for x in tokenised_sent]
    
    lengthlist = []
    
    for i in x:
        lengthlist.append(len(i))
    stdeviation = numpy.std(lengthlist)
    return stdeviation

def folder_sent_std(folder_path, output_path):
    file_names = os.listdir(folder_path)
    
    file_name_and_text = {}
    
    for file in file_names:
        with open(folder_path + file, "r") as target_file:
            file_name_and_text[file] = target_file.read()
            
    length_list = []
    for key in file_name_and_text:
        length_list.append(sent_std(file_name_and_text[key]))
        
    zip_iterator = zip(file_names, length_list)
    a_dictionary = dict(zip_iterator)
    
    df = pd.DataFrame(data=a_dictionary, index=[0])
    df = (df.T)
    df.to_excel(output_path)

    print (df)



    

folder_path = 'ENTER THE LOCATION OF THE FOLDER WITH INPUT FILES'
output_path = 'ENTER THE LOCATION FOR YOUR OUTPUT FILE'


folder_sent_std(folder_path, output_path)






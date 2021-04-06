# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 


filepathin = 'FILE PATH HERE'

import os

file_names = os.listdir(filepathin)



# Create Dictionary for File Name and Text
file_name_and_text = {}
for file in file_names:
    with open(filepathin + file, "r") as target_file:
         file_name_and_text[file] = target_file.read()

#file_data = (pd.DataFrame.from_dict(file_name_and_text, orient='index').reset_index().rename(index = str, columns = {'index': 'file_name', 0: 'text'}))
#file_dataframe = pd.DataFrame(file_name_and_text)

for key in file_name_and_text:
    
    split_string = file_name_and_text[key].split("WORDS TO DELETE EVERYTHING AFTER", 1)
    file_name_and_text[key] = split_string[0]   
    file_name_and_text[key] = file_name_and_text[key].replace('SOME WORDS', '')


#import csv

#with open('/Users/sabis_home_folder/Desktop/mycsvfile.csv','w') as f:
        #w = csv.writer(f)
        #w.writerows(file_name_and_text.items())
 

dictwithsplit = {k:list(v.split()) for k,v in file_name_and_text.items()}
     
newdict = { }

for k, v in dictwithsplit.items():
    newdict[k] = []
    start_index = 0 
    end_index = 500
    
    while start_index < len(v):
        if end_index > len(v):
            end_index = len(v)
        chunk = slice(start_index, end_index)
        newdict[k].append(v[chunk])
        

        start_index = end_index
        end_index += 500 #split into 500 words chunks
        
def ToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 



for ke, va in newdict.items(): #tokens back to string in lists in dict
    newdict[ke] = [ToString(x) for x in newdict[ke]]
    
for k,v in newdict.items(): # generating files
    filename = k.replace('.txt','_')
    path = 'FILE PATH OUT' 
    for line in v:
        chunkfilename = filename + 'ch_' + str(v.index(line)) # setting name generator
        with open(os.path.join(path, chunkfilename), 'w') as fp: 
            fp.write(line)
        
    

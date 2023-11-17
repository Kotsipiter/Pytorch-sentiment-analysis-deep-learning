import pandas as pd
import numpy as np
import nltk





text = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
filename = "F:\Program Files (x86)\Pytorch sentiment analysis deep learning\sample text.txt"
 
 
def remove_punc(string):
    punc = '''()-[]{}:'"\,<>/@#$%^&*_~'''
    punc_to_be_replaced = '?!'
    for ele in string:  
        
        if ele in punc:  
            string = string.replace(ele, "")
        if ele in punc_to_be_replaced:
            string = string.replace(ele,".")
        words = set(nltk.corpus.words.words())

        sent = "Io andiamo to the beach with my amico."
        " ".join(w for w in nltk.wordpunct_tokenize(sent) \
                if w.lower() in words or not w.isalpha())
    return string
 
 
try:
    with open(filename,'r',encoding="utf-8") as f:
        data = f.read()
    with open(filename,"w+",encoding="utf-8") as f:
        f.write(remove_punc(data))
    print("Removed punctuations from the file", filename)
except FileNotFoundError:
    print("File not found")

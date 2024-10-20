# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:00:30 2024

@author: Vivek
"""

'''
Q3.Use stemming for following docs
doc = nlp("Mando talked for 3 hours although talking isn't his thing")
doc = nlp("eating eats eat ate adjustable rafting ability meeting better")
'''
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from spacy.symbols import ORTH

# Load the English tokenizer
nlp = English()

# Define a custom function for stemming
def custom_stem(token):
    # Example stemming rule: convert "eating" to "eat"
    if token.lower_ == "eating":
        return "eat"
    # Add more stemming rules as needed
    # For example: handle different tenses of verbs
    # elif token.lower_ == "talked":
    #     return "talk"
    else:
        return token.lower_

# Apply the custom function to each token in the document
def apply_custom_stemming(doc):
    return [custom_stem(token) for token in doc]

# Define the documents
docs = [
    "Mando talked for 3 hours although talking isn't his thing",
    "eating eats eat ate adjustable rafting ability meeting better"]

# Process each document and apply stemming
for text in docs:
    doc = nlp(text)
    stemmed_tokens = apply_custom_stemming(doc)
    print(" ".join(stemmed_tokens))

#Output
'''
mando talked for 3 hours although talking is n't his thing
eat eats eat ate adjustable rafting ability meeting better
'''

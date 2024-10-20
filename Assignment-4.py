# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:01:49 2024

@author: Vivek
"""
'''
Q4. convert these list of words into base form using Stemming and Lemmatization and observe the transformations 
 
#using stemming in nltk
lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']
#using lemmatization in spacy
doc = nlp("running painting walking dressing likely children who good ate fishing")

'''
import nltk
from nltk.stem import PorterStemmer
import spacy

# Initialize NLTK's Porter Stemmer
stemmer = PorterStemmer()

# List of words for stemming
lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']

# Apply stemming using NLTK
stemmed_words_nltk = [stemmer.stem(word) for word in lst_words]

# Print the results
print("Stemming using NLTK:")
for original, stemmed in zip(lst_words, stemmed_words_nltk):
    print(f"{original} -> {stemmed}")

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Apply lemmatization using spaCy
doc = nlp(" ".join(lst_words))
lemmatized_words_spacy = [token.lemma_ for token in doc]

# Print the results
print("\nLemmatization using spacy are:")
for original, lemmatized in zip(lst_words, lemmatized_words_spacy):
    print(f"{original} -> {lemmatized}")

#Output:
'''
Stemming using NLTK:
running -> run
painting -> paint
walking -> walk
dressing -> dress
likely -> like
children -> children
whom -> whom
good -> good
ate -> ate
fishing -> fish

Lemmatization using spacy are:
running -> run
painting -> paint
walking -> walk
dressing -> dress
likely -> likely
children -> child
whom -> whom
good -> good
ate -> eat
fishing -> fishing

'''

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:49:32 2024

@author: Vivek
"""

'''
Q1.convert the given text into it's base form using both stemming
 and lemmatization
text = """Latha is very multi talented girl.She is good at many skills
 like dancing, running, singing, playing.She also likes eating Pav Bhagi.
 she has a habit of fishing and swimming too.Besides all this,
 she is a wonderful at cooking too.
"""
'''

import spacy

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Define the text
text = """ 
Latha is very multi talented girl.She is good at many skills
 like dancing, running, singing, playing.She also likes eating Pav Bhagi.
 she has a habit of fishing and swimming too.Besides all this,
 she is a wonderful at cooking too.
 """

# Process the text with spaCy
doc = nlp(text)

# Lemmatize the text
lemmatized_text = " ".join(token.lemma_ if token.lemma_ != "-PRON-" else token.text for token in doc)

print(lemmatized_text)

#Output:
'''
Latha be very multi talented girl . she be good at many skill 
like dancing , running , singing , play . she also like eat Pav Bhagi . 
she have a habit of fishing and swim too . besides all this , 
she be a wonderful at cook too . 
'''

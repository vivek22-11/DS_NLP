# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:51:32 2024

@author: Vivek
"""


"""
Q2.You are parsing a news story from cnbc.com. News story is 
stores in news_story.txt which is on whatsapp. You need to, 
1.Extract all NOUN tokens from this story. You will have to read
 the file in python first to collect all the text and then extract
 NOUNs in a python list
2.Extract all numbers (NUM POS type) in a python list
3.Print a count of all POS tags in this story
""" 
import spacy

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Read the news story from the file
with open("C:/Assignments/NLP/news_story.txt", "r", encoding="utf-8") as file:
    news_text = file.read()

# Process the text with spaCy
doc = nlp(news_text)

# 1. Extract all NOUN tokens
nouns = [token.text for token in doc if token.pos_ == "NOUN"]

# 2. Extract all numbers (NUM POS type)
numbers = [token.text for token in doc if token.pos_ == "NUM"]

# 3. Print a count of all POS tags
pos_counts = {}
for token in doc:
    pos_counts[token.pos_] = pos_counts.get(token.pos_, 0) + 1

print("NOUN tokens:", nouns)
print("Numbers:", numbers)
print("POS tag counts:", pos_counts)

#Output:
'''
print("NOUN tokens:", nouns)
NOUN tokens: ['News', 'form', 'information', 'people', 'events', 'range', 'topics', 'politics', 'economics', 'society', 'culture', 'News', 'mediums', 'newspapers', 'television', 'radio', 'platforms', 'purpose', 'public', 'events', 'developments', 'issues', 'lives']

print("Numbers:", numbers)
Numbers: []

print("POS tag counts:", pos_counts)
POS tag counts: {'PUNCT': 18, 'NOUN': 23, 'AUX': 4, 'DET': 3, 'ADP': 6, 'PRON': 5, 'VERB': 9, 'ADJ': 7, 'ADV': 4, 'CCONJ': 5, 'PART': 1}
'''

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 09:24:49 2022

@author: Ellen
"""

import nltk
import re
import numpy as np
import pandas as pd

#### Opening the file

poems2_df=pd.read_excel("C:/Python/project/Clean_Poems.xlsx", engine="openpyxl", header=0)

#### Create data frame for words - tokenize process
poem_words = pd.DataFrame()

#### Small sample
poems2_df_sample =  poems2_df.sample(frac=0.5, replace=False, random_state=1)
poems2_df_sample

#### Elaborate process for all poems: 
    
for index, row in poems2_df_sample.iterrows(): #if you apply a sample, it is necessary to change this part to: poems2_df_sample
    # Create strign with each poem
    cell = row['Content']
    # execute the text here as :
    text = cell
    dataset = nltk.sent_tokenize(text)

    # Clean the poem 
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = re.sub(r'\W', ' ', dataset[i])
        dataset[i] = re.sub(r'\s+', ' ', dataset[i])

    # Create a dictionary with the number of times word appears in a given poem
    word2count = {}
    for data in dataset:
        words = nltk.word_tokenize(data)
        for word in words:
            if word not in word2count.keys():
                word2count[word] = 1
            else:
                word2count[word] += 1

    # Create different dataframes
    exec('poem_words_{} = pd.DataFrame([word2count], index=[ {} ])'.format(index, index))
    
    # Append rows in a single dataframe
    exec('poem_words = poem_words.append(poem_words_{})'.format(index))
    
    # Replace nans with zero
    poem_words_final = poem_words.fillna(0)
    print(poem_words_final)
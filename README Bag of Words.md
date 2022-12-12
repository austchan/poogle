# Bag of words

In this document, we will explain the actions that were codyfied to create a bag of words. 

1. How to run this code? 

You can find the code with the name "Bag of words"

2. What the script does?

This script creates a bag of words considering the poems. The objective is creating a matrix of vectors which represents the words and the numbers of time that these words appear. To do this, the first step is import the packages: nltk, re, and nump. After this, the next step is open the data and create a sample of 50% of observations where we will work. Then, we apply some process to confirm that the data is clean. Next step is create a dictionary with the number of times word appears in a given poem; we use nltk.word_tokenize and word2count. Finally, we create a matrix which has all vectors that represents the bag of words. 

### Import parckages

import nltk
import re
import numpy as np
poem_words = pd.DataFrame()

#### Opening the file

poems2_df=pd.read_excel("C:/Python/project/Clean_Poems.xlsx", engine="openpyxl", header=0)

#### Create data frame for words - tokenize process
poem_words = pd.DataFrame()

#### Small sample
#poems2_df_sample =  poems2_df.sample(frac=0.01, replace=False, random_state=1)
#poems2_df_sample

#### Elaborate process for all poems: 
    
for index, row in poems2_df.iterrows(): #if you apply a sample, it is necessary to change this part to: poems2_df_sample
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

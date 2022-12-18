# Cleaning the Dataframe

In this module, we will focus on cleaning the poems as obtained in a Pandas dataframe. The objective is to create a column with poem stanzas
that are lowercase, stripped of punctuation and stopwords, and lemmatised. This would enable further analysis of the stanzas.

1. First we need to convert the column containing the stanzas ('Content') to strings. We would also need to drop any blank cells to avoid any errors. 
2. We would then lowercase all characters for uniformity and remove any punctuation. 
3. This would be followed by importing stopwords from nltk and removing those from the stanzas.
4. This would be followed by tokenisation and lemmatised of the text. 

This would finally be saved and converted to a XLS format for Step 3: Bag of Words

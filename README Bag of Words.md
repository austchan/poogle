# Bag of words

In this document, we will explain the actions that were codyfied to create a bag of words. 

1. How to run this code? 

You can find the code with the name "Bag of words"

2. What the script does?

This script creates a bag of words considering the poems. The objective is creating a matrix of vectors which represents the words and the numbers of time that these words appear. To do this, the first step is import the packages: nltk, re, and nump. After this, the next step is open the data and create a sample of 50% of observations where we will work. Then, we apply some process to confirm that the data is clean. Next step is create a dictionary with the number of times word appears in a given poem; we use nltk.word_tokenize and word2count. Finally, we create a matrix which has all vectors that represents the bag of words. 


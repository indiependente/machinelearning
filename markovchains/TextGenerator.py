
# coding: utf-8

# In[7]:

import nltk
import random


file = open('divina_commedia.txt', 'r')
words = file.read()
words = words.split()


# In[8]:

def makePairs(arr):
    return [(arr[i], arr[i+1]) for i in xrange(len(arr)-1)]


# In[9]:

'''
model: conditional frequency distribution,
word: starting word,
num: numbers of words to generate
'''
def generate(model, word = 'the', num = 50):
    for i in range(num):
        arr = []
        for j in model[word]:
            for k in xrange(int(model[word][j])):
                arr.append(j)

        print word.decode('unicode-escape'),

        word = arr[int(len(arr)*random.random())]


# In[10]:

pairs = makePairs(words)
model = nltk.ConditionalFreqDist(pairs)
generate(model, word = 'come', num = 1000)


# In[ ]:




import nltk
import random


def makePairs(arr):
    return [(arr[i], arr[i+1]) for i in xrange(len(arr)-1)]


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




if __name__ == '__main__':
	import sys
	filename = sys.argv[1]
	file = open(filename, 'r')
	words = file.read()
	words = words.split()

	firstWord = sys.argv[2]
	numWords = int(sys.argv[3])

	pairs = makePairs(words)
	model = nltk.ConditionalFreqDist(pairs)
	generate(model, word = firstWord, num = numWords)







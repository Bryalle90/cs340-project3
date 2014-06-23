import sys
import time
import random

class Node:
	def __init__(self):
		self.wordEnd = False
		self.ptr = dict()

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, key):
		curr = self.root
		for c in key:
			if c not in curr.ptr:
				curr.ptr[c] = Node()
			curr = curr.ptr[c]
		curr.wordEnd = True

	def printTrie(self):
		if not self.root == None:
			curr = self.root
			wordString = ''
			self.p(curr, wordString)

	def p(self, curr, wordString):
		if curr.wordEnd:
			print wordString
		for c in curr.ptr:
			self.p(curr.ptr[c], wordString + c)







infile = open( './dictionaryLin.txt', 'r')
wordlist = []
mysteryWord = 'sabby'
searchlist = [ 'circuitry', 'grecize', 'legislative assembly', 'primuline yellow', 'terephthalate', 'widest dissemination', 'zamiel']
wlSize = 20

for i, item in enumerate( infile ):
	wordlist.append(item)
	if i >= wlSize:
		break

random.shuffle(wordlist)
# wordlist.sort( key= lambda x: len( x ), reverse= True )

trie = Trie()

### Start timing inserts
tInsert_start = time.clock()
for w in wordlist:
	trie.insert(w[:-1])
tInsert_end = time.clock()

trie.printTrie()
from Trie import *
from math import *
from otherMethods import *
import sys

#getting data from config
conf = open('config.csv')
params = {}
for line in conf:
	a = line.split(",")
	a[1] = a[1][:-1]
	params[a[0]] = a[1]

inFile = "input.csv"
outFile = "output.csv"
flag = int(params["flag"])
minsup = float(params["support"])
mincon = float(params["confidence"])


singletons = {}
noOfTransactions = 0;
infp = open(inFile)
for a in infp:
	a = a.strip()
	b = a.split(",")
	for i in b:
		if i in singletons:
			singletons[i] = singletons[i] + 1
		else:
			singletons[i] = 1
	noOfTransactions += 1
	
#print singletons
freqSingles = []
freqSinglesCount = []

for i in singletons:
	minTransactions = ceil(noOfTransactions * minsup)
	if singletons[i] >= minTransactions:
		a = [i]
		freqSingles.append(a)
		freqSinglesCount.append(singletons[i])

#print freqSingles
#print freqSinglesCount
FreqsTrie = trieNode()

FreqsTrie.insertAll(freqSingles, freqSinglesCount)
#print FreqsTrie.child

freqSingles.sort()
FreqItemSets = freqSingles;
currSizeList = freqSingles;


allfreqs = len(currSizeList)
while True:
	#print currSizeList
	
	nextSizeList = generate(currSizeList)
	prunedList = prune(FreqsTrie, nextSizeList)
	if len(prunedList) == 0:
		break

	counts = itemSetsCount(inFile, prunedList)
#	print counts
	FreqItems = []
	FreqCounts = []

	size = len(prunedList)
	for i in range(size):
		if counts[i] >= minTransactions:
#			print "Aravind"
			FreqItems.append(prunedList[i])
			FreqCounts.append(counts[i])

	if len(FreqCounts) == 0:
#		print "Hey"
		break

	FreqsTrie.insertAll(FreqItems, FreqCounts)
	currSizeList = FreqItems
	allfreqs += len(currSizeList)

#sys.stdout = open("output.csv", 'w')
print allfreqs
print FreqsTrie.printAll("")

#sys.stdout.close()
#print FreqsTrie.child['1'].child

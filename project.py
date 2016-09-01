from Trie import *
from math import *
from otherMethods import *
import sys
import itertools
import sets
import fileinput
import time

#getting data from config
start = time.time()

conf = open('config.csv')
params = {}
for line in conf:
	a = line.split(",")
	a[1] = a[1][:-1]
	params[a[0]] = a[1]

inFile = params["input"]
outFile = params["output"]
flag = int(params["flag"])
minsup = float(params["support"])
mincon = float(params["confidence"])

sys.stdout = open(outFile, 'w')

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
	
freqSingles = []
freqSinglesCount = []

print "FreqCount"

for i in singletons:
	minTransactions = ceil(noOfTransactions * minsup)
	if singletons[i] >= minTransactions:
		a = [i]
		print i
		freqSingles.append(a)
		freqSinglesCount.append(singletons[i])

freqSingles.sort()

FreqsTrie = trieNode()
FreqsTrie.insertAll(freqSingles, freqSinglesCount)

FreqItemSets = freqSingles;
currSizeList = freqSingles;

allfreqs = len(currSizeList)

while True:
	nextSizeList = generate(currSizeList)
	prunedList = prune(FreqsTrie, nextSizeList)
	if len(prunedList) == 0:
		break

	counts = itemSetsCount(inFile, prunedList)
	FreqItems = []
	FreqCounts = []

	size = len(prunedList)
	for i in range(size):
		if counts[i] >= minTransactions:
			print (",").join(prunedList[i])
			FreqItems.append(prunedList[i])
			FreqCounts.append(counts[i])

	if len(FreqCounts) == 0:
		break

	FreqsTrie.insertAll(FreqItems, FreqCounts)
	currSizeList = FreqItems
	allfreqs += len(currSizeList)

if flag == 1:
	print "RulesCount"
	noOfRules = printAssociateRules(FreqsTrie, mincon)

#print time.time() - start
sys.stdout.close()

for line in fileinput.input(outFile,inplace=1):
    if "RulesCount" in line and flag == 1:
        line=line.replace(line,str(noOfRules) + "\n")
    elif "FreqCount" in line:
    	line=line.replace(line,str(allfreqs) + "\n")
    print line,



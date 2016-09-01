from Trie import *
from math import *
from otherMethods import *
import sys
import itertools
import sets
import fileinput

#getting data from config
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

sys.stdout = open("output.csv", 'w')

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

print "FreqCount"

for i in singletons:
	minTransactions = ceil(noOfTransactions * minsup)
	if singletons[i] >= minTransactions:
		a = [i]
		print i
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
			print (",").join(prunedList[i])q
			FreqItems.append(prunedList[i])
			FreqCounts.append(counts[i])

	if len(FreqCounts) == 0:
#		print "Hey"
		break

	FreqsTrie.insertAll(FreqItems, FreqCounts)
	currSizeList = FreqItems
	allfreqs += len(currSizeList)

#print allfreqs
#FreqsTrie.printAll("")
print "RulesCount"
noOfRules = printAssociateRules(FreqsTrie, mincon)
sys.stdout.close()

for line in fileinput.input("output.csv",inplace=1):
    if "RulesCount" in line:
        line=line.replace(line,str(noOfRules) + "\n")
    elif "FreqCount" in line:
    	line=line.replace(line,str(allfreqs) + "\n")
    print line,

"""
for i in FreqsTrie.getItemSets([]):
	for j in range(1, len(i)):
		for k in itertools.combinations(i, j):
			if float(FreqsTrie.getCount(i)) / float(FreqsTrie.getCount(k)) >= mincon:
				print (',').join(k) + "=>" + (',').join(set(i) - set(k))



"""
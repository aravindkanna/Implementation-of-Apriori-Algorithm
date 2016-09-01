from sets import Set
import itertools


def generate(currentSizeList):
	size = len(currentSizeList)
	i = 0
	j = 1

	nextSizeList = []
	while i < size:
		j = i + 1
		while j < size:
			a = []
			if currentSizeList[i][:-1] == currentSizeList[j][:-1]:
				a = currentSizeList[i][:]
				a.append(currentSizeList[j][-1])
				nextSizeList.append(a)
				j += 1
			else :
				break
		i += 1

	return nextSizeList

def oneLessSubsets(itemset):
	allSubsets = []
	size = len(itemset)
	for i in range(size):
		s = itemset[:i] + itemset[i+1:]
		allSubsets.append(s)
	return allSubsets

def prune(FreqsTrie, currList):
	prunedList = []
	for i in currList:
		allSubsets = oneLessSubsets(i)
		flag = True
		for j in allSubsets:
			if not FreqsTrie.hasNode(j):
				flag = False
				break
		if flag:
			prunedList.append(i)
	return prunedList

def itemSetsCount(inFile, currList):
	infp = open(inFile)
	counts = []
	size = len(currList)
	for i in range(size):
		counts.append(0)
	for line in infp:
		line = line.strip()
		itemList = line.split(",")
		currTransaction = Set(itemList)
		currSize = len(currTransaction)
		for i in range(size):
			a = currList[i][:]
			sz = len(a)
			if currSize < sz:
				continue 
			itemSet = Set(a)
			if currTransaction.issuperset(itemSet):
				counts[i] += 1
	return counts

def printAssociateRules(FreqsTrie, mincon):
	count = 0
	for i in FreqsTrie.getItemSets([]):
		for j in range(1, len(i)):
			for k in itertools.combinations(i, j):
				if float(FreqsTrie.getCount(i)) / float(FreqsTrie.getCount(k)) >= mincon:
					print (',').join(k) + "=>" + (',').join(set(i) - set(k))
					count += 1
	return count

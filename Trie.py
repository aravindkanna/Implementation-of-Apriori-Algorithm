from Queue import *

"""
class trie:
	def __init__(self):
		self.root = {}
		self.count = 1

	#l is a list of trienodes
	def insertNode(self, l):
		f = self.root
		for i in l:
			if i in f:
				f = f[i]
			else:
				f[i] = {}
				f = f[i]

	def deleteNode(self, l):
		f = self.root
		pre = {}
		for i in l:
			if i in l:
				pre = f
				f = f[i]
			else:
				return

		pre.pop(i, None)

	def hasNode(self, l):
		f = self.root
		for i in l:
			if i in f:
				f = f[i]
			else:
				return False
		return True

#	def printAll(self):

"""

class trieNode:
	def __init__(self, count = 1, name = "root"):
		self.child = {}
		self.count = count
		self.name = name

	def insertNode(self, itemset, count):
		f = self.child
		for i in itemset:
			if i in f:
				f = f[i].child
			else:
				temp = trieNode(count, i)
				f[i] = temp

	def hasNode(self, itemset):
		f = self.child
		for i in itemset:
			if i in f:
				f = f[i].child
			else:
				return False
		return True

	#FreqItemSets is a dictionary
	def insertAll(self, FreqItemSets, counts):
		size = len(FreqItemSets)
		for i in range(size):
			self.insertNode(FreqItemSets[i], counts[i])

	def printAll(self, prevStr):
		for i in self.child:
			a = prevStr + i
			print a
			self.child[i].printAll(a + ",")

	def getItemSets(self, prevList):
		for i in self.child:
			a = prevList+[i]
			yield a
			for j in self.child[i].getItemSets(a):
				yield j

	def getCount(self, itemSet):
		f = self.child
		for i in itemSet:
			fp = f[i]
			f = f[i].child
		return fp.count
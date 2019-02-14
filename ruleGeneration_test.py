#call functions of the file and this file only for ruleGeneration
#the use of a hash table superdict which was created in gen_powerset.py which has the support of all frequent candidates has been made to find support in O(1) time.
#we also use the fact that all subsets of a frequent candidate shall be frequent to avoid hitting the data set 

import pickle
import copy

pkl_file = open("superdict.pkl","rb")
superdict = pickle.load(pkl_file)
item = []

def generateAllRules(x,y,used,item):
	x = list(x)
	y = list(y)
	if len(x) > 1:
		inum = 0
		for i in x:
			x_made = []
			x_made = x[:]
			y_made = y[:]
			y_made.append(x[inum])
			y_made.sort()
			del x_made[inum]
			tmp = tuple(y_made)
			try:
				used[tmp] == 1
			except KeyError:
				if confidence(item,y_made) > minconfidence:
					x_made = tuple(x_made)
					y_made = tuple(y_made)
					finalRules[x_made] = y_made
					generateAllRules(x_made,y_made,used,item)
			inum = inum + 1
			return

def confidence(supab,supb):
	supab.sort()
	supb.sort()
	global max
	max = 0
	supab = tuple(supab)
	supb = tuple(supb)
	result = superdict[supab][0]/superdict[supb][0]
	if result > max:
		max = result
		print(supab,supb,result)
	return result

minconfidence = 0.03
finalRules = {}


def relevantRule(item):
	inum = 0
	for i in item:
		y = []
		x = item[:]
		used = {}
		y.insert(-1,item[inum])
		del x[inum]
		inum = inum+1
		if confidence(item,y) > minconfidence:
			x = tuple(x)
			y = tuple(y)
			used[y] = 1
			finalRules[x] = y
			generateAllRules(x,y,used,item)


def callme():

	# relevantRule([4,6,8,20,27])
	for i in superdict:
		if len(i) > 1:
			item = list(i)
			relevantRule(item)


callme()
print(finalRules)
print(max)
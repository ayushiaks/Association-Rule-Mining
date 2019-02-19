#call functions of the file and this file only for ruleGeneration
#the use of a hash table superdict which was created in gen_powerset.py which has the support of all frequent candidates has been made to find support in O(1) time.
#we also use the fact that all subsets of a frequent candidate shall be frequent to avoid hitting the data set 

import pickle
import copy

pkl_file = open("../pkl_files/superdict.pkl","rb")
superdict = pickle.load(pkl_file)
item = []
pkl_file = open("../pkl_files/hash_table.pkl","rb")
hash_table = pickle.load(pkl_file)

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
				con = confidence(item,x_made)
				if con >= minconfidence:
					x_made = tuple(x_made)
					y_made = tuple(y_made)
					finalRules[x_made] = (y_made,con)
					generateAllRules(x_made,y_made,used,item)
			inum = inum + 1
			return

def confidence(supab,supb):
	supab.sort()
	supb.sort()
	supab = tuple(supab)
	supb = tuple(supb)
	result = superdict[supab][0]/superdict[supb][0]
		# print(supab,supb,result)
	return result

minconfidence = 0.1
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
		con = confidence(item,x)
		if con > minconfidence:
			x = tuple(x)
			y = tuple(y)
			used[y] = 1
			finalRules[x] = (y,con)
			generateAllRules(x,y,used,item)


def callme():
	# relevantRule([4,6,8,20,27])
	for i in superdict:
		if len(i) > 1:
			item = list(i)
			relevantRule(item)


callme()
print(len(finalRules))
for i in finalRules:
	l = list(i)
	x = []
	for j in l:
		x.append(hash_table[j])
	l = list(finalRules[i])
	l = l[0]
	y = []
	for j in l:
		y.append(hash_table[j])
	if len(y) >= 1:
		print(x,"->",y)

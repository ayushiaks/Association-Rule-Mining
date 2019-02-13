#call functions of the file and this file only for ruleGeneration
#the use of a hash table superdict which was created in gen_powerset.py which has the support of all frequent candidates has been made to find support in O(1) time.
#we also use the fact that all subsets of a frequent candidate shall be frequent to avoid hitting the data set 

import pickle

pkl_file = open("superdict.pkl","rb")
superdict = pickle.load(pkl_file)

def generateAllRules(lvl_rules):
	#call this function len-1 times here itself
	#and pass rules of each level
	i = len(lvl_rules)
	lvh_rules = []
	flag = False
	while i > 0:
		if len(lvl_rules[i-2]) > 1:
			x_maker = lvl_rules[i-2]
			y_maker = lvl_rules[i-1]
			inum = 0
			for aman in x_maker: 
				x = x_maker
				y = y_maker
				y.insert(-1,x_maker[inum])
				del x[inum]
				inum = inum +1
				if confidence(x,y)>minconfidence:
					lvh_rules.append(x)
					lvh_rules.append(y)
					flag = True
					x = tuple(x)
					y = tuple(y)
					finalRules[x] = y
		i = i-2

		if flag:
			generateAllRules(lvh_rules)
		else:
			break
	return

def confidence(supab,supb):
	supab.sort()
	supb.sort()
	supab = tuple(supab)
	supb = tuple(supb)
	result = superdict[supab][0]/superdict[supb][0]
	return result

minconfidence = 0.01
finalRules = {}

lvl_rules = []
	#find x and y refering to silde l9-s9
def relevantRule(item):
	inum = 0
	for i in item:
		y = []
		x = item
		y.insert(-1,item[inum])
		del x[inum]
		inum = inum+1		
		if confidence(x,y) > minconfidence:
			lvl_rules.append(x)
			lvl_rules.append(y)
			x = tuple(x)
			y = tuple(y)
			finalRules[x] = y


def callme():
	for i in superdict:
		if len(i) > 1:
			aman = list(i)
			relevantRule(aman)
	generateAllRules(lvl_rules)


callme()
# print(superdict)
# for i in finalRules:

	# if len(finalRules[i]) > 1:
	# 	print(i,"->",finalRules[i])
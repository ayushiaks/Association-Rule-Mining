"""
This generates rules with given minconfidence(default = 0.8) 
"""

#call functions of the file and this file only for ruleGeneration
#the use of a hash table superdict which was created in gen_powerset.py which has the support of all frequent candidates has been made to find support in O(1) time.
#we also use the fact that all subsets of a frequent candidate shall be frequent to avoid hitting the data set 

import pickle
import copy

pkl_file = open("../pkl_files/superdict.pkl","rb")
superdict = pickle.load(pkl_file)
item = []
pkl_file.close()
pkl_file = open("../pkl_files/hash_table.pkl","rb")
hash_table = pickle.load(pkl_file)
pkl_file.close()
#it is a recurssive functions which takes in lv1 rules as input and generate rules for rest of generations
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
					finalRules.append([x_made,y_made,con])
					generateAllRules(x_made,y_made,used,item)
			inum = inum + 1
			return

#calculates confidence for a rule
def confidence(supab,supb):
	supab.sort()
	supb.sort()
	supab = tuple(supab)
	supb = tuple(supb)
	result = superdict[supab][0]/superdict[supb][0]
	return result

#taking input minconfidence
minconfidence = 0.8
minc = input("minconfidence(btw 0 and 1)= ")
minconfidence = float(minc)
finalRules = []


#this function generates lv1 rules and calls generateAllRules to generate rest of the rules
def lv1_rules(item):
	inum = 0
	for i in item:
		y = []
		x = item[:]
		used = {}
		y.insert(-1,item[inum])
		del x[inum]
		inum = inum+1
		con = confidence(item,x)
		
		if con >= minconfidence:
			x = tuple(x)
			y = tuple(y)
			used[y] = 1
			finalRules.append([x,y,con])
			generateAllRules(x,y,used,item)

#this function passed a frequent itemset and all rules above minconfidence are generated
#it calls lv1_rules() which further calls other functions
def ruleGeneration():
	for i in superdict:
		if len(i) > 1:
			item = list(i)
			lv1_rules(item)


ruleGeneration()




#used to print things to understand the code
with open('rules.txt','w') as f:
	for i in finalRules:
		con = i[2]
		sup1=superdict[i[0]][0]
		sup2=superdict[i[1]][0]
		l1=[]
		for j in list(i[0]):
			l1.append(hash_table[j])
		l2=[]
		for j in list(i[1]):
			l2.append(hash_table[j])	
		
		

		string = str([l1,(sup1),"->",l2,(sup2), con])
		f.write(string)
		f.write("\n")


print(len(finalRules))
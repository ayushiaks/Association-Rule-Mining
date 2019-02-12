import pickle
import numpy as np
from powerset import *
from generate import k_itemset 

pkl_file=open("items.pkl","rb")

items=pickle.load(pkl_file)

hash_table=dict()

count=1
for i in items_list:
	hash_table[count]=i
	count=count+1

def support(lists):
	try:
   		intersected = set(lists[0]).intersection(*lists)
	except ValueError:
		intersected = set()
	return len(intersected)

superdict = dict()

for i in hash_table:
	superdict[(i)]=[support([items[hash_table[i]]]),1]

true_candidates = []
candidates=	[]

for i in superdict:
	l=[i]
	candidates.append(l)
k_itemset(candidates,1)
# for i in items_list:
# 	superdict=

# for i in range(1,len(items_list)):
# 	l=powerset(items_list,i)
# 	k_itemset(l,i)
for i in superdict:
	k = superdict[i]
	if k[1]!=-1:
		l = powerset(i, k[1]-1)
		for j in l:
			if  tuple(j) in superdict:
				if superdict[tuple(j)][1]==-1:
					superdict[i][1] = -1
					break
			else:
				superdict[i][1] = -1
print(superdict)
  
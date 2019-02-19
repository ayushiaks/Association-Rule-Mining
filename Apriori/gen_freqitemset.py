"""
This code generates frequent itemsets using inbuilt functions and k-itemset generation function from merge_itemsets.py
The dictionary of frequent itemsets contains the count and length of the itemset
"""

import pickle
import numpy as np
from powerset import powerset,lsupport
from merge_itemsets import k_itemset 

pkl_file=open("../pkl_files/items.pkl","rb")
items=pickle.load(pkl_file)
pkl_file.close()

s=input("Enter min support:")
min_sup=int(s)

items_list=[]

for item in items:
	if lsupport(min_sup, items[item]):
		items_list.append(item)

#gives an id to each frequent item
hash_table=dict()

count=1
for i in items_list:
	hash_table[count]=i
	count=count+1

max_length=len(items_list)

def csupport(lists):
	try:
   		intersected = set(lists[0]).intersection(*lists)
	except ValueError:
		intersected = set()
	return len(intersected)

superdict = dict()

for i in hash_table:
	l = [i]
	superdict[tuple(l)]=[csupport([items[hash_table[i]]]),1]

true_candidates = []
candidates=	[]

for i in hash_table:
	l=[i]
	candidates.append(l)

for i in range(1,max_length):
	true_candidates=[]
	candidates=k_itemset(candidates,i)
	for j in candidates:
		flag = 1
		l = powerset(j, len(j)-1)
		for p in l:
			if  tuple(p) in superdict:
				continue
			else:
				flag=0
				break
		if flag==1:
			sup=[]
			for k in j:
				sup.append(items[hash_table[k]])
			if csupport(sup)>min_sup:
				superdict[tuple(j)]=[csupport(sup),len(j)]
				true_candidates.append(j)
						
	candidates=true_candidates		

print(len(superdict))

pkl_file = open("../pkl_files/superdict.pkl","wb")
pickle.dump(superdict,pkl_file)
pkl_file.close()
pkl_file = open("../pkl_files/hash_table.pkl", "wb")
pickle.dump(hash_table,pkl_file)
pkl_file.close()
  

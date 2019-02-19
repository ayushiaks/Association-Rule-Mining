import pickle
import numpy as np
from powerset import *
from merge_itemsets import k_itemset 

pkl_file=open("../pkl_files/items.pkl","rb")

items=pickle.load(pkl_file)

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
print(candidates)

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
			if csupport(sup)>=20:
				superdict[tuple(j)]=[csupport(sup),len(j)]
				true_candidates.append(j)
						
	candidates=true_candidates		

pkl_file = open("../pkl_files/superdict.pkl","wb")
pickle.dump(superdict,pkl_file)
pkl_file = open("../pkl_files/hash_table.pkl", "wb")
pickle.dump(hash_table,pkl_file)
pkl_file.close()
  

import pickle
import numpy as np

pkl_file=open("items.pkl","rb")

items=pickle.load(pkl_file)

# print(items)

def powerset(s, k):
	x = len(s)
	powerset = []
	list = None
	for i in range(1, 1 << x):
		list = [s[j] for j in range(x) if (i & (1 << j))]
		if len(list) == k:
			powerset.append(list)
	return powerset

def support(minsup,l):
	if len(l)>=minsup:
		return True
	return False

items_list=[]

#DM KI ASS: Dict se delete krnaa h
for item in items:
	if support(1000, items[item]):
		items_list.append(item)

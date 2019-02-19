

import pickle

pkl_file=open("../pkl_files/items.pkl","rb")

items=pickle.load(pkl_file)


def powerset(s, k):
	x = len(s)
	powerset = []
	list = None
	for i in range(1, 1 << x):
		list = [s[j] for j in range(x) if (i & (1 << j))]
		if len(list) == k:
			powerset.append(list)
	return powerset

def lsupport(minsup,l):
	if len(l)>minsup:
		return True
	return False



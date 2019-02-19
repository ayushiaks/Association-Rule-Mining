"""
This code takes in a list(k) and value of k in k-itemset(_itemset) and returns a list of all possible k-itemsets
It prunes the supersets if subsets are found to be non-frequent except in the case mentioned below, that is taken care of in gen_freqitemset.py
"""

#abcd abde are there then no need for generating abcde as abce is did not qualify 
#in this case only one false case shall qualify 
#when abcd and abce exist which shall be later removed

def k_itemset(k,_itemset):
	newk= []
	length = len(k)
	x =0
	if(_itemset>=2):
		for i in range(length-1):
			for j  in range(i+1,length):
				flag = True
				tmp = []
				for x in range(_itemset-1):
					if k[i][x] != k[j][x]:
						flag = False
						break
					else:
						tmp.append(k[i][x])
				x = x+1
				if 	flag:	
					tmp.append(k[i][x])
					tmp.append(k[j][x])
				if 	flag and (len(tmp) == _itemset+1):
					newk.append(tmp)
	else:
		for i in range(length-1):
			for j in range(i+1,length):
				tmp=[]
				tmp.append(k[i][0])
				tmp.append(k[j][0])
				newk.append(tmp)
	return newk

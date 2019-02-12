import numpy as np


#abcd abde are there then no need for generating abcde as abce is did not qualify 
#in this case only one false case shall qualify 
#when abcd and abce exist which shall be later removed

def k_itemset(k,_itemset):
	newk= []
	length = len(k)
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
			if 	flag:	
				tmp.append(k[i][x+1])
				tmp.append(k[j][x+1])
			if 	flag and (len(tmp) == _itemset+1):
				newk.append(tmp)
	return newk

k = [[2,3,4,6],[2,3,5,9],[2,3,9,10]]
k = k_itemset(k,4)
print(k)

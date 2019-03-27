"""
This code takes input all frequent itemsets and finds closed itemsets 
"""

import pickle
import copy
from itertools import combinations

pkl_file = open("./pkl_files/superdict.pkl","rb")
superdict = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open("./pkl_files/hash_table.pkl","rb")
hash_table = pickle.load(pkl_file)
pkl_file.close()

closed_list = superdict.copy()

index = {}
_list = []
k = 1
l_list = []

#for every length of the transactions
for i in closed_list:
    if closed_list[i][1] == k:
        index[k] = i
        l_list.append(i)
    else:
        k += 1
        index[k] = i
        _list.append(l_list)
        l_list = []


redundant_item = []
for k in range(0,len(_list)-1):
    for i in _list[k]:
        for j in _list[k+1]:
            if closed_list[tuple(i)][0] == closed_list[tuple(j)][0]:
                a = [word for word in i if word not in j]
                if len(a) == 0:
                    closed_list[tuple(i)][1] = 0
                    redundant_item.append(i)


#find and write all closed itemsets in a file
_closed = []
print(redundant_item)
for i in closed_list:
    if closed_list[i][1] != 0:
        _closed.append(i)

closed = []
for i in _closed:
    closed_list = []
    for j in i:
        closed_list.append(hash_table[j])
    closed.append(closed_list)

pkl_file = open("./pkl_files/closed.pkl","wb")
pickle.dump(closed,pkl_file)
pkl_file.close()

#write all redundant itemsets in a file
pkl_file = open("./pkl_files/redundant_item.pkl","wb")
pickle.dump(redundant_item,pkl_file)
pkl_file.close()

print(len(closed),"closed")
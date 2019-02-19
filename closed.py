"""
Written by: Garvit
Written on: Feb 18,2019
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

tmp = superdict.copy()

index = {}
_list = []
k = 1
l_list = []
for i in tmp:
    if tmp[i][1] == k:
        index[k] = i
        l_list.append(i)
    else:
        k += 1
        index[k] = i
        _list.append(l_list)
        l_list = []

for k in range(0,len(_list)-1):
    for i in _list[k]:
        for j in _list[k+1]:
            if tmp[tuple(i)][0] == tmp[tuple(j)][0]:
                # print(i,j)
                a = [word for word in i if word not in j]
                # print(a)
                if len(a) == 0:
                    print("asd")
                    tmp[tuple(i)][1] = 0
                    # continue
                    print(i,j,tmp[tuple(i)][0],tmp[tuple(j)][0])
_closed = []
for i in tmp:
    if tmp[i][1] != 0:
        _closed.append(i)

closed = []
for i in _closed:
    tmp = []
    for j in i:
        tmp.append(hash_table[j])
    closed.append(tmp)
print(closed)

pkl_file = open("./pkl_files/closed.pkl","wb")
pickle.dump(closed,pkl_file)
pkl_file.close()
print(len(closed),"closed")


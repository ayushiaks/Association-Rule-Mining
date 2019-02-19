"""
Written by: Garvit
Written on: Feb 17,2019
This code takes input all frequent itemsets and finds maximal itemsets 
"""
#makes maximal powerset using superdict in a specific-general approach

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

def checkSet(temp):
    _list = []
    for i in range(len(temp)-1,0,-1):
        _list = list(combinations(temp,i))
        for j in _list:
            x = tuple(j)
            tmp[x][1] = 0

def generateMaximal():
    _list = []
    max = 0
    for i in tmp:
        if tmp[i][1] > max:
            max = tmp[i][1]
    temp = []
    for i in tmp:
        if tmp[i][1] != 0:
            temp = list(i)
            checkSet(temp)
    _list = []
    for i in tmp:
        if tmp[i][1] != 0:
            _list.append(i)
    return _list

ans = generateMaximal()
maximal = []
for i in ans:
    tmp = []
    for j in i:
        tmp.append(hash_table[j])
    maximal.append(tmp)

print(maximal,"ds")
print(len(maximal),"maximal")

pkl_file = open("./pkl_files/maximal.pkl","wb")
pickle.dump(maximal,pkl_file)
pkl_file.close()


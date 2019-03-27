"""
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

superdict_copy = superdict.copy()

def checkSet(temp):
    _list = []
    for i in range(len(temp)-1,0,-1):
        _list = list(combinations(temp,i))
        for j in _list:
            x = tuple(j)
            superdict_copy[x][1] = 0

def generateMaximal():
    _list = []
#     max = 0
#     for i in tmp:
#         if tmp[i][1] > max:
#             max = tmp[i][1]
    temp = []
    for i in superdict_copy:
        if superdict_copy[i][1] != 0:
            temp = list(i)
            checkSet(temp)
    _list = []
    for i in superdict_copy:
        if superdict_copy[i][1] != 0:
            _list.append(i)
    return _list

ans = generateMaximal()
maximal = []
for i in ans:
    maximal_item = []
    for j in i:
        maximal_item.append(hash_table[j])
    maximal.append(maximal_item)

print(maximal)
print(len(maximal),"maximal")

pkl_file = open("./pkl_files/maximal.pkl","wb")
pickle.dump(maximal,pkl_file)
pkl_file.close()

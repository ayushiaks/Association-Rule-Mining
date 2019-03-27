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

maximal_list = superdict.copy()

#breaks each transaction into its subset and remove them from maximal set
def checkSet(transaction):
    _list = []
    for i in range(len(transaction)-1,0,-1):
        _list = list(combinations(transaction,i))
        for j in _list:
            x = tuple(j)
            maximal_list[x][1] = 0

#finds all maximal itemsets
def generateMaximal():
    _list = []
    transaction = []
    for i in maximal_list:
        if maximal_list[i][1] != 0:
            transaction = list(i)
            checkSet(transaction)
    _list = []
    for i in maximal_list:
        if maximal_list[i][1] != 0:
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

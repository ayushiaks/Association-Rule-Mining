#makes maximal powerset using superdict in a specific-general approach

import pickle
import copy
from itertools import combinations

pkl_file = open("./pkl_files/superdict.pkl","rb")
superdict = pickle.load(pkl_file)

tmp = superdict.copy()

def callmelater(temp):
    _list = []
    for i in range(len(temp)-1,0,-1):
        _list = list(combinations(temp,i))
        # print(_list)
        for j in _list:
            x = tuple(j)
            # print(x)
            tmp[x][1] = 0

def callme():
    length = (len(tmp))
    _list = []
    max = 0
    maximal_list = []
    for i in tmp:
        if tmp[i][1] > max:
            max = tmp[i][1]
    # print(max)
    temp = []
    for i in tmp:
        if tmp[i][1] != 0:
            temp = list(i)
            callmelater(temp)
    _list = []
    for i in tmp:
        if tmp[i][1] != 0:
            _list.append(i)
    print(len(_list))
    print(len(tmp))
    return _list

ans = callme()
pkl_file = open("./pkl_files/maximal.pkl","wb")
pickle.dump(ans,pkl_file)
pkl_file.close()

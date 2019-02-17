import pickle
import copy
from itertools import combinations

pkl_file = open("superdict.pkl","rb")
superdict = pickle.load(pkl_file)

tmp = superdict.copy()


def checksub(t1,t2):
    c = 0
    for i in t1:
        for j in t2:
            if i == j:
                c = c+1
                # print(i,j)
                if len(t1) == c:
                    print("y")
                    return True
    else:
        print("fy",c)
        return False

# checksub((1,2),(1,2,3))

def nameme():
    # listi = {}
    # listj = {}
    for i in tmp:
        for j in tmp:
            if len(j)>len(i):
                if len(j) < 3:
                    print(i,j)
                    # if tmp[i][0] == tmp[j][0]:
                    #     print(i,j)
                    #     if checksub(i,j) == True:
                    #         print(i,j,len(j),len(i))

    #     listi[i] = 0
    #     listj[i] = 0
    # for i in tmp:
    #     itmp = listi.copy()
    #     for k in i:
    #         itmp[k] = 1
    #     # print(listi)
    #     for j in tmp:
    #         jtmp = listj.copy()
    #         for kj in j:
    #             jtmp[kj] = 1
    #         if len(j) > len(i):
    #             continue
                
nameme()
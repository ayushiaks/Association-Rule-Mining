import pickle

pkl_file=open("transactions.pkl","rb")
transactions=pickle.load(pkl_file)

pkl_file=open("items.pkl","rb")
items=pickle.load(pkl_file)


pkl_file=open("hash.pkl","rb")
hash_table=pickle.load(pkl_file)

pkl_file=open("reverse_hash.pkl","rb")
reverse_hash_table=pickle.load(pkl_file)

class Tree(object):
    "Generic tree node."
    def __init__(self, name=0,parent=None,children=None):
        self.name = name
        self.children = {}
        if 'p' not in self.children:
            self.children['p']=parent
        # self.parent = parent
        # self
    def repr(self):
        return self.name
    def add_child(self, node,parent):
        self.children[node]=[1,Tree(node,parent),parent]
    def child(self):
        return self.children
    # def parent(self):
    #     print(self.parent)
    #     return self.parent
    def update(self, node):
        self.children[node][0]=self.children[node][0]+1

root = Tree(0,0)
# root.add_child(1)
# root.add_child(2)
# temp = root.child()[2][1]
# temp.add_child(3)

pointers = {}
# transactions = {}
# transactions[1] = [1, 2]
# transactions[2] = [2, 3]

count = 0
store = []


for i in transactions:
    temp = root
    # print(transactions[i])
    for j in transactions[i]:
        if j not in store:
            count = count+1
            store.append(j)
        if j not in temp.child():
            temp.add_child(j,temp)
            temp = temp.child()[j][1]
        else:
            temp.update(j)
            temp = temp.child()[j][1]
        val = j
        if val in pointers:
            l = pointers[val]
            l.append(temp)
            pointers[val] = l
        else:
            l = []
            l.append(temp)
            pointers[val] = l
# print(root)
# print(root.child()['p'])
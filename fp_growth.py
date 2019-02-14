import pickle

pkl_file=open("transactions.pkl","rb")
transactions=pickle.load(pkl_file)

pkl_file=open("hash.pkl","rb")
hash_table=pickle.load(pkl_file)

pkl_file=open("reverse_hash.pkl","rb")
reverse_hash_table=pickle.load(pkl_file)

class Tree(object):
    "Generic tree node."
    def __init__(self, name=0, children=None):
        self.name = name
        self.children = {}
    def repr(self):
        return self.name
    def add_child(self, node):
        self.children[node]=[1,Tree(node)]
    def child(self):
        return self.children
    def update(self, node):
        self.children[node][0]=self.children[node][0]+1

root = Tree(0)
# root.add_child(1)
# root.add_child(2)
# root.update(2)
# l=root.child()

# l[1][1].add_child(3)
# l[1][1].add_child(4)

# print(root.child())
# print(l[1][1].child())



for i in transactions:
    temp = root
    print(transactions[i])
    for j in transactions[i]:
        if j not in temp.child():
            temp.add_child(j)
            temp = temp.child()[j][1]
        else:
            temp.update(j)
            temp = temp.child()[j][1]
    
print(reverse_hash_table[8])
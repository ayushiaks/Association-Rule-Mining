"""
why does it exists 
"""
import pickle
import time

start=time.time()

pkl_file=open("../pkl_files/transactions.pkl","rb")
transactions=pickle.load(pkl_file)

pkl_file=open("../pkl_files/reverse_hash.pkl","rb")
reverse_hash=pickle.load(pkl_file)

class Tree(object):
    """Generic tree node.
        Name:The value of node
        Children:Points to dictionary for which value of key is its (Frequency,Address of its node,Address of the parent)
        Repr:Function which returns name of the node
        Add_Child:Function to add child of a node
        Child: Function which returns a dictionary that contains the Children of th node
        Update: Function to increase the count by 1 when it is encountered again    
    """
    def __init__(self, name=0,parent=None,children=None):
        self.name = name
        self.children = {}
        if 'p' not in self.children:
            self.children['p']=parent
    def repr(self):
        return self.name
    def add_child(self, node,parent):
        self.children[node]=[1,Tree(node,parent),parent]
    def child(self):
        return self.children
    def update(self, node):
        self.children[node][0]=self.children[node][0]+1


def make_tree(transactions,min_sup):
    """This function takes a dictionary(Transaction Id: [The number of items purchased]) and minimum support as input.
       It returns FP Tree for this transaction, Header Table, Items(In sorted order which are in the tree)   
    """
    items={}

    # Makes a dictionary of all the items in transaction with its count i.e. Key is item and Support count is its value
    for i in transactions:
        for j in transactions[i]:
            if j not in items:
                items[j]=1
            else:
                items[j]=items[j]+1
    
    #Deleting the less frequent items
    items_copy=items.copy()
    for i in items_copy:
        if items[i]<min_sup:
            del(items[i])
    
    #Sorting Items according to support count
    items_list=[]
    for i in items:
        items_list.append(i)

    def sortSecond(val): 
        return items[val]

    items_list.sort(key = sortSecond,reverse = True)
    
    #Ordering the transactions according to sorted order which is required for FP Growth Algorithm 
    true_transactions={}
    for i in transactions:
        for j in items_list:
            if j in transactions[i]:
                if i in true_transactions:
                    true_transactions[i].append(j)
                else:
                    true_transactions[i]=[j]

    #Construction of FP tree
    root = Tree(0,0)
    pointers = {}
    for i in true_transactions:
        temp = root
        for j in true_transactions[i]:
            if j not in temp.child():
                temp.add_child(j,temp)
                temp = temp.child()[j][1]
            else:
                temp.update(j)
                temp = temp.child()[j][1]
            val = j
            if val in pointers:
                l = pointers[val]
                if temp not in l:
                    l.append(temp)
                    pointers[val] = l
            else:
                l = []
                l.append(temp)
                pointers[val] = l

    return root,pointers,items_list

def prefix(pointers,val):
    """ Returns every prefix path of the node which is passed to it. Now this prefix path will be used as transaction to make
        conditional FP tree on the passed node   
    """
    prefix_path={}
    count=1
    for j in pointers[val]: 
        path_ = []
        leng=j.child()['p'].child()[j.repr()][0]
        while j.child()['p']!=0:
            j = j.child()['p']
            if j.repr()!=0:
                path_.append(j.repr())
        if len(path_)!=0:
            path_.reverse()
            for i in range(leng):
                prefix_path[count]=path_
                count=count+1

    return prefix_path




def mine_tree(root,pointers,items_list, min_support, prefix_, freq_item_list):
    """ Recursive function to mine tree according Condition Patteren Bases
        Conditional Fp tree is again passed to make FP_Tree
    """
    items_list.reverse()
    
    for item in items_list:
        new_freq_set = prefix_.copy()
        new_freq_set.add(item)
        freq_item_list.append(new_freq_set)
        cond_pattern_bases = prefix(pointers,item)
        cond_tree, head ,i_list= make_tree(cond_pattern_bases, min_support)

        if head != None:
            mine_tree(cond_tree, head,i_list,min_support, new_freq_set, freq_item_list)

def fp_tree(min_sup):
    root,pointers,items_list=make_tree(transactions,min_sup)

    freq_items = []
    mine_tree(root, pointers,items_list,min_sup, set([]), freq_items)


    freq_actual=[]
    for i in freq_items:
        l=[]
        for j in i:
            l.append(reverse_hash[j])
        freq_actual.append(l)
    return freq_actual
    
freq_actual=fp_tree(int(input("Enter the minimum support you want for FP_Tree:")))
end=time.time()
print("Time Taken:",end-start)
# for i in freq_actual:
#         print(i)    
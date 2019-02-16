import pickle
# from gen_powerset import hash_table
from powerset import items_list
import pandas
import numpy as np

data_file = "groceries.csv"

pkl_file=open("items.pkl","rb")

items=pickle.load(pkl_file)

data_file_delimiter = ','

# The max column count a line in the file could have
largest_column_count = 0

# Loop the data lines
with open(data_file, 'r') as temp_f:
    # Read the lines
    lines = temp_f.readlines()

    for l in lines:
        # Count the column count for the current line
        column_count = len(l.split(data_file_delimiter)) + 1

        # Set the new most column count
        largest_column_count = column_count if largest_column_count < column_count else largest_column_count

# Close file
temp_f.close()

# Generate column names (will be 0, 1, 2, ..., largest_column_count - 1)
column_names = [i for i in range(0, largest_column_count)]

# Read csv
df = pandas.read_csv(data_file, header=None, delimiter=data_file_delimiter, names=column_names)


df = df.fillna('')

df=df.values

size=df.shape

print(size)

transactions = {}
count = 1
hash_table = {}
reverse_hash_table={}

for i in range(size[0]):
	transaction_list = []
	for j in range(size[1]):
		if df[i][j]!='':
			if df[i][j] not in hash_table:
				# print(cont)
				hash_table[df[i][j]] = count
				reverse_hash_table[count]=df[i][j]
				count = count+1
			transaction_list.append(hash_table[df[i][j]])
			
	transactions[i+1] = transaction_list

# print(reverse_hash_table)

print(transactions[3])

def sortSecond(val): 
    return len(items[val])


print(items_list)
items_list.sort(key = sortSecond,reverse = True)
# print(len(items['napkins']),len(items['whole milk']))


sorted_list=[]
for i in items_list:
	sorted_list.append(hash_table[i])

print(sorted_list)

true_transactions={}

for i in transactions:
	for j in sorted_list:
		if j in transactions[i]:
			if i in true_transactions:
				true_transactions[i].append(j)
			else:
				true_transactions[i]=[j]

print(true_transactions[3])
output=open("transactions.pkl",'wb')
pickle.dump(true_transactions,output)
output.close()

output=open("hash.pkl",'wb')
pickle.dump(hash_table,output)
output.close()

output=open("reverse_hash.pkl",'wb')
pickle.dump(reverse_hash_table,output)
output.close()
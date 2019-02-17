from fp_growth import *
# from operator import itemgetter

pkl_file=open("sorted_list.pkl","rb")
sorted_list=pickle.load(pkl_file)

sorted_list.reverse()

# print(sorted_list)
# print(pointers[140][0].child()['p'])
def intersect(lists):
	try:
   		intersected = set(lists[0]).intersection(*lists)
	except ValueError:
		intersected = set()
	return len(intersected)

prefix_path={}

for i in sorted_list:
# count = 0

	path = []
	# print(len(pointers[140]))
	for j in pointers[i]: 
	# 	print(type(j))
	# 	# print(j.child())
	# 	print(j.child()['p'])
		path_ = []
		while j.child()['p']!=0:
			j = j.child()['p']
			path_.append(j.repr())
		path_.reverse()
		if len(path_)!=0:
			path.append(path_)
	prefix_path[i]=path

print((prefix_path[140]))

for i in prefix_path:
	freq = []
	n = len(prefix_path[i])
	# for j in prefix_path[i]:

	# print(freq)

	


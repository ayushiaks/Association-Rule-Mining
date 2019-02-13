#call functions of the file and this file only for ruleGeneration
#the use of a hash table superdict which was created in gen_powerset.py which has the support of all frequent candidates has been made to find support in O(1) time.
#we also use the fact that all subsets of a frequent candidate shall be frequent to avoid hitting the data set 

# pkl_file = open("superdict.pkl","rb")
# superdict = pickle.load(pkl_file)
superdict = {}
superdict[] = 6
superdict[1] = 6

def confidence(supab,supb):
	result = superdict[supab]/superdict[supb]
	# result = supab/supb
	return result

# minconfidence = 0.5

# for item in superdict:
	#find x and y refering to silde l9-s9
def relevantRule(item):
	c = ''
	for i in item:
		c += (str(i))
	# allRules = generateAllRules(c)
	lv1_rules = []
	for i in range(len(c)):
		x = c[:i]+c[i+1:]
		y = c[i]
		print(x,y)
		if confidence(x,y) > minconfidence:
			rule = x+"->"+y
			lv1_rules.append()

# a = confidence(7,2)
# print(a)
relevantRule([1,3,4])
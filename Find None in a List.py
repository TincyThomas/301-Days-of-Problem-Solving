def find_none(lst):
	for i in lst:                           # looping elements of input
		if i == None:                         # checking whether i equals to None
			return lst.index(None)              # return index of None
		else:
			return -1                           # if there is no none then return -1
print(find_none([None,0, 1, 2, 3, 4]))

def num_of_sublists(lst):
	count = 0
	for i in lst:
		if type(i)==int:
			return "0"
		else:
			count+=1
	return count
print(num_of_sublists([1, 2, 3]))

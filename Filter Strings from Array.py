def filter_list(l):
	a = []
	for i in l:
		if type(i) == int:
			a = a+[i]
	return a
print(filter_list([1, 2, "7", "fav", 3, "a", "b", 4]))

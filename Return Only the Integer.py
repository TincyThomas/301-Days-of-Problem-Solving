def return_only_integer(lst):
	a= []
	for i in lst:
		if type(i) == int:
			a = a +[i]
	return a
print(return_only_integer([9, 2, "space", "car", "lion", 16]))

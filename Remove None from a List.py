def remove_none(lst):
	a = []
	for i in lst:
		if i != None:
			a = a+[i]
	return a
print(remove_none(["a", None, "b", None]))

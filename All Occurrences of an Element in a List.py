def get_indices(lst, el):
	count = -1
	a = []
	for i in lst:
		count += 1
		if i==el:
			a +=[count]
	return a
print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))

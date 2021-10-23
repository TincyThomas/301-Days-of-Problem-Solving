def unique_lst(lst):
	a = []
	for i in lst:
		if i>0:
			a = a + [i]
	return set(a)
print(unique_lst([-5, 1, -7, -5, -2, 3, 3, -5, -1, -1]))

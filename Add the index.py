def add_indexes(lst):
	a = []
	count = -1
	for i in lst:
		count = count + 1
		a = a + [count+i]
	return a
print(add_indexes([0, 0, 0, 0, 0]))

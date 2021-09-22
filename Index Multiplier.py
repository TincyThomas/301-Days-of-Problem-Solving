def index_multiplier(lst):
	ind = -1
	a = 0
	for i in lst:
		ind = ind + 1
		a = a + (i*ind)
	return a
print(index_multiplier([1, 2, 3, 4, 5]))

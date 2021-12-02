def sum_fractions(lst):
	a = 0
	for i in lst:
		a += i[0]/i[1]
	return int(a)
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))

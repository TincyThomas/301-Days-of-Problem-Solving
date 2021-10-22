def cumulative_sum(lst):
	a = 0
	lis = []
	for i in lst:
		a = a + i
		lis = lis + [a]
	return lis
print(cumulative_sum([1, 2, 3]))

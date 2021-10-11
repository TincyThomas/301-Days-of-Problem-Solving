def sum_two_smallest_nums(lst):
	a = min(lst)
	lst.remove(a)
	b = min(lst)
	return a + b
print(sum_two_smallest_nums([19, 5, 42, 2, 77]))

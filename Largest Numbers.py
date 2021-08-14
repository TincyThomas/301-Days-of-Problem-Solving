def largest_numbers(n, lst):
	a = [max(lst)]
	for i in range(1,n):
		ls = lst.pop(lst.index(max(lst)))
		a = a + [max(lst)]
	return a
print(largest_numbers(1, [7, 19, 4, 2]))

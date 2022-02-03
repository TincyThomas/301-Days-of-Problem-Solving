def largest_even(lst):
	a = 0
	for i in lst:
		if i%2==0:
			if i>a:
				a=i
			else:
				continue
	return a
print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))

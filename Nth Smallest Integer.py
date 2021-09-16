def nth_smallest(lst, n):
	lst.sort()
	return lst[n-1]
print(nth_smallest([7, 3, 8, 1], 2))

def reverse(lst):
	a = []                                  # empty list
	for i in lst:                           # looping input
		a = [i] + a                           # placing it ahead
	return a
print(reverse([9, 9, 2, 3, 4]))

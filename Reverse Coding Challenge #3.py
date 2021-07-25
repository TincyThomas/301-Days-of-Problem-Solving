def mystery_func(lst, n):
	a = []
  for i in lst:
		a = a+ [i%n]
	return a
print(mystery_func([5, 7, 8, 2, 1], 2))

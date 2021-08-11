def odd_product(lst):
	a = 1
	for i in lst:
		if i%2!=0:
			a = a*i
	return a
print(odd_product([3, 4, 1, 1, 5]))

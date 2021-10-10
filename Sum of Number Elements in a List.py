def numbers_sum(lst):
	a = 0
	for i in lst:
		if type(i) ==int:
			a = a + i
	return a
print(numbers_sum([1, 2, 3, 4, 5, True]))

def sum_missing_numbers(lst):
	a = 0
	for i in range(min(lst),max(lst)):
		if i in lst:
			continue
		else:
			a +=i
	return a
print(sum_missing_numbers([1, 2, 3, 4, 5]))

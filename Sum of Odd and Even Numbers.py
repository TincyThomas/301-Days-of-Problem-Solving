def sum_odd_and_even(lst):
	e = 0
	o = 0
	for i in lst:
		if i%2==0:
			e +=i
		else:
			o +=i
	return [e,o]
print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))

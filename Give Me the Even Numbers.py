def sum_even_nums_in_range(start, stop):
	a =0
	for i in range(start,stop+1):
		if i %2==0:
			a = a+i
	return a
print(sum_even_nums_in_range(10, 20))

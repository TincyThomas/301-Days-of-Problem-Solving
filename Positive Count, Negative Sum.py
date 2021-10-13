def sum_neg(lst):
	sum = 0
	count = 0
	for i in lst:
		if i > 0:
			count = count + 1
		else:
			sum = sum + i
	return [count,sum]
print(sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]))

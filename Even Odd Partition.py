def even_odd_partition(lst):
	even =[]
	odd = []
	for i in lst:
		if i%2==0:
			even = even+[i]
		else:
			odd = odd+[i]
	return [even, odd]
print(even_odd_partition([5, 8, 9, 2, 0]) )

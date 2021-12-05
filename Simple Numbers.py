def simple_numbers(a, b):
	count= 0
	q = 0
	res = []
	for i in range(a,b):
		for x in str(i):
			count +=1
			q+=int(x)**count
		count = 0
		if q == i:
			res+=[q]
		q = 0
	return res
print(simple_numbers(90, 100))

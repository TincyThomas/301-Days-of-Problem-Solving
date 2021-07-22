def list_sum(lst):
	a = []
	for i in lst:
		if i%2==0:
			a = a+[i*i]
		else:
			a =a +[(i)**(1/2)]
	k =0
	for j in a:
		k = k + j
	return round(k,2)
print(list_sum([1, 3, 3, 1, 10]))

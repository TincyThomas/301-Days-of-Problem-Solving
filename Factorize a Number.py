def factorize(num):
	a = []
	for i in range(1,int(num/2)+1):
		if num%i==0:
			a = a + [i]
	return a + [num]
print(factorize(17))

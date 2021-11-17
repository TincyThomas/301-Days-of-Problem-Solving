def divisible_by_left(n):
	l = [False]
	a = []
	for i in str(n):
		a = a + [i]
	for j in range(0,len(a)-1):
		if int(a[j+1])%int(a[j])==0:
			l = l + [True]
		else:
			l = l + [False]
	return l
print(divisible_by_left(635))

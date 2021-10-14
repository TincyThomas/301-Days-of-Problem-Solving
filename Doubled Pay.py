def doubled_pay(n):
	a = []
	q = 1
	sum =0
	for i in range(0,n):
		a = a + [q]
		q = q*2
	for j in a:
		sum =sum +j
	return sum
print(doubled_pay(3))

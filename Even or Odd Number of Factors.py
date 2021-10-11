def factor_group(num):
	q = []
	for i in range(1,num+1):
		if num%i == 0:
			q = q + [i]
		else: continue
	return "even" if len(q)%2==0 else "odd"
print(factor_group(33))

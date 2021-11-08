def gcd(n1, n2):
	one = [n1]
	two = [n2]
	for i in range(1,int(n1/2)+1):
		if n1%i==0:
			one = one+[i]
		else:
			continue
	for i in range(1,int(n2/2)+1):
		if n2%i==0:
			two = two+[i]
		else:
			continue
	lst3 = [value for value in one if value in two]
	return max(lst3)
print(gcd(17, 13))

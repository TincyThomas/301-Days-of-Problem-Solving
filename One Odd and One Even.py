def one_odd_one_even(n):
	a = str(n)
	first = int(a[0])
	second = int(a[1])
	if (first%2==0 and second%2!=0) or (second%2==0 and first%2!=0):
		return True
	else: return False
print(one_odd_one_even(21))

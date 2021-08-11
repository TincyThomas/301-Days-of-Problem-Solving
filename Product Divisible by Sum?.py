def divisible(lst):
	a = 0
	b = 1
	for i in lst:
		a = a+i
		b=b*i
		return True if b%a==0 else False
print(divisible([3, 2, 4, 2]))

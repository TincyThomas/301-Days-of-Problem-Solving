def is_harshad(n):
	a = 0
	for i in str(n):
		a+=int(i)
	return True if n%a==0 else False
print(is_harshad(171))

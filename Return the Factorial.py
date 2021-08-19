def factorial(num):
	a = num
	while num > 1:
		a =  a *(num-1)
		num = num -1
	return a
print(factorial(3))

def two_digit_sum(n):
	a = 0
	for i in str(n):
		a = a+ int(i)
	return a
print(two_digit_sum(45))

def count_ones(num):
	r  = ''
	count = 0
	while num >0:
		rem = num % 2
		if rem == 1:
			count = count +1
		num = int(num/2)
	return count
print(count_ones(999))
	

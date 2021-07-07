def find_factors(n):
	a = []                                    # empty list
	for i in range(1,int(n/2)+1):             # looping till half of n elements... to save computation time
		if n%i==0:                              # checking divisibility 
			a = a + [i]                           # concatenating i
	return a + [n]                            # we know number is always divisible by it own
print(find_factors(8))

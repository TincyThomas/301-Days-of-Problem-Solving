def parity(n):
	remainder = bool(n % 2)               # evaluating bool of when taken modulo 
	if remainder == False:                # check like 4%2 = 0, denotes false in boolean
		return "even"                       # that is even
	else:
		return "odd"
print(parity(0))

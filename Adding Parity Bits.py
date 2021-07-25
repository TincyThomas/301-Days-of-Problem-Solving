def add_parity_bit(b):
	a =str(b)
	q = a.count("1")
	if q%2==0:
		return str(b)+"1"
	else:
		return str(b)+"0"
print(add_parity_bit("10110111"))

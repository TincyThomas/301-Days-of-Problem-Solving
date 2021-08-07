def has_hidden_fee(prices, t):
	a = 0
	for i in prices:
		b = i[1:]
		a = a+int(b)
	if a == int(t[1:]):
		return True
	else:
		return False
print(has_hidden_fee(["$2", "$1", "$4", "$8"], "$15"))

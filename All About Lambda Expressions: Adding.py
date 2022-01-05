def adds_n(n):
	return lambda a : n + a

adds1=adds_n(1)
print(adds1(5.7))

def last_dig(a, b, c):
	res = str(a * b)
	return True if res[-1]==str(c)[-1] else False
print(last_dig(55, 223, 5190))

def simple_encoder(s):
	index = -1
	a = ""
	for i in s:
		count = s.count(i)
		index = index+1
		if count == 1:
			a = a+"["
		else:
			a = a + "]"
	return a
print(simple_encoder("Mubashir"))

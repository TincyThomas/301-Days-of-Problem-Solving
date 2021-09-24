def cap_to_front(s):
	a = ""
	b = ""
	for i in s:
		if i.isupper():
			a = a + i
		else:
			b= b + i
	return a+b
print(cap_to_front("hApPy"))

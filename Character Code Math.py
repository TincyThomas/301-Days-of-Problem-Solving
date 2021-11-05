def calc(s):
	a = ""
	b = ""
	for i in s:
		a = a + str(ord(i))
	for i in a:
		if i == "7":
			b = b + "1"
		else:
			b = b + i
	t = eval(a) - eval(b)
	q = 0
	for i in str(t):
		q = q + int(i)
	return q
print(calc("ifkhchlhfde"))

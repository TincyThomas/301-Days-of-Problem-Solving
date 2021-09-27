def ascii_capitalize(txt):
	a = ""
	for i in txt:
		if ord(i) %2 == 0:
			a= a + i.upper()
		else:
			a= a + i.lower()
	return a
print(ascii_capitalize("to be or not to be!"))

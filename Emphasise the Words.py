def emphasise(txt):
	a = txt.split(" ")
	b = []
	for i in a:
		b += [i[0].upper()+i[1:].lower()]
	return " ".join(b)
print(emphasise("99 red balloons!"))

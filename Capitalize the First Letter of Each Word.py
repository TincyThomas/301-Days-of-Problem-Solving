def make_title(txt):
	b = []
	a = txt.split(" ")
	for i in a:
		b = b + [i[0].upper()+i[1:]]
	return " ".join(b)
print(make_title("This is a title"))

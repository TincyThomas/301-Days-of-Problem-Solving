def shhh(txt):
	a = ""
	x = txt[0].upper()
	for i in txt[1:]:
		a = a + i.lower()
	return x+a+ ", whispered Edabit."
print(shhh("HI THERE!"))

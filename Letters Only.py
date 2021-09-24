def letters_only(txt):
	a = ""
	for i in txt:
		if i.isupper() or i.islower():
			a = a + i
		else:
			continue
	return a
print(letters_only("^U)6$22>8p)."))

def detect_word(txt):
	a = ''
	for i in txt:
		if i.islower():
			a = a+i
	return a
print(detect_word("UcUNFYGaFYFYGtNUH"))

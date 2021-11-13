def century(year):
	s = str(year)
	if s[-2:]=="00":
		return s[0:2] + "th century"
	else:
		return str(int(s[0:2])+1)+"th century"
print(century(2005))

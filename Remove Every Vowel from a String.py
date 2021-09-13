def remove_vowels(txt):
	a = ""
	for i in txt:
		if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
			a = a + ""
		else:
			a =a + i
	return a
print(remove_vowels("We're gonna build a wall!"))

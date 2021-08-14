def first_vowel(txt):
	count = -1
	for i in txt:
		count = count + 1
		if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U":
			return count
print(first_vowel("STRAWBERRY"))

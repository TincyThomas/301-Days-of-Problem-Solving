def count_vowels(txt):
	count = 0
	for i in txt:
		if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or i == "o" or i == "O" or i == "u" or i == "U":
			count = count +1
	return count
print(count_vowels("Celebration"))

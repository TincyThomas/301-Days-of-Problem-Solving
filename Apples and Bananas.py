def vow_replace(word, vowel):
	vow = ["a","e","i","o","u"]
	a = ""
	for i in word:
		if i in vow:
			a = a + vowel
		else:
			a = a + i
	return a
print(vow_replace("stuffed jalapeno poppers", "e"))

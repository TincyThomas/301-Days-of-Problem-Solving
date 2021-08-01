def strip_sentence(txt, chars):
	a = ""
	for t in txt:
		if t not in chars:
			a = a+t
	return a
print(strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou"))

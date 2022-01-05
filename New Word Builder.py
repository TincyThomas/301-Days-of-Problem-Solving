def word_builder(ltr, pos):
	a = []
	for i in pos:
		a+=ltr[i]
	return "".join(a)
print(word_builder(["g", "e", "o"], [1, 0, 2]))

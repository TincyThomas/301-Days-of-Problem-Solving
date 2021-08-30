def index_of_caps(word):
	count = -1
	a = []
	for i in word:
		count = count + 1
		if i.isupper():
			a = a + [count]
		else:
			continue
	return a
print(index_of_caps("sUnnY"))

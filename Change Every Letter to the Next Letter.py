def move(word):
	b = ""
	for i in word:
		a = ord(i)+1
		b +=chr(a)
	return b
print(move("hello"))

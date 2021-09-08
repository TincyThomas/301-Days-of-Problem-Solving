def is_isogram(txt):
	a = len(set(txt))
	b = len(txt)
	if a == b:
		return True
	else:
		return False
print(is_isogram("Apple"))

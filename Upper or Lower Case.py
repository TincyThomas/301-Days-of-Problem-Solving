def steps_to_convert(txt):
	u = 0
	l = 0
	for i in txt:
		if i.isupper():
			u = u + 1
		elif i.islower():
			l = l + 1
	if l<u:
		return l
	else:
		return u
print(steps_to_convert("abCCC"))

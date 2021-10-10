def reverse(txt):
	a = ""
	for i in txt:
		a = i + a
	return a
print(reverse("world"))

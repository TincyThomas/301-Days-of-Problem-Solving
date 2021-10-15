def reverse(txt):
	a = txt.split(" ")
	if len(a) == 1:
		return txt[::-1]
	else:
		return txt
print(reverse("This"))

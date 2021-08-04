def reverse_title(txt):
	t = txt[0].lower()
	t1= txt[1:len(txt)].upper()
	return t+t1
print(reverse_title("this is a title"))

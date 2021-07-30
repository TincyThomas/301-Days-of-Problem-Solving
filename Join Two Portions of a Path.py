def join_path(portion1, portion2):
	count = -1
	a = portion1
	b = portion2
	for i in portion1:
		count = count +1
		if i == "/":
			a = portion1[:count]
	if portion2[0] == "/":
		b = portion2[1:]
	return a+"/"+b
print(join_path("portion1", "/portion2"))

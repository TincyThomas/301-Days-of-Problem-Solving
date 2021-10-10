def remove_abc(txt):
	qw = ""
	if "a" not in txt or "b" not in txt or "c" not in txt:
		return None
	else:
		for i in txt:
			if i == "a" or i =="b" or i == "c":
				continue
			else:
				qw = qw + i

		return qw
print(remove_abc("hello world!"))

def stmid(string):
	a = string.split(" ")
	b  = ""
	for i in a:
		if len(i) % 2 == 0:
			b = b + i[0]
		else:
			b = b + i[int(len(i)/2)]
	return b
print(stmid("Alexa have to paid"))

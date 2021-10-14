def secret(text):
	txt = text[:len(text)-2]
	a = "<" + txt + ">" + "<"+ "/" + txt + ">"
	return a * int(text[-1])
print(secret("li*3"))

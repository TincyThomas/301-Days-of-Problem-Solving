def maskify(txt):
	t = len(txt)-4
	e = txt[t:]
	q = txt[:t]
	a=len(q)
	return "*"*a+e
print(maskify("455636"))

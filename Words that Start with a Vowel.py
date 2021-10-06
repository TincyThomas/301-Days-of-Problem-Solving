def retrieve(txt):
	vow = []
	a = txt.lower().split(" ")
	v = ["a","e","i","o","u"]
	for j in a:
		if j[0] in v:
			vow = vow + [j]
	return vow
print(retrieve("A simple life is a happy life for me."))

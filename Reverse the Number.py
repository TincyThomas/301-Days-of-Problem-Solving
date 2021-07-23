def rev(n):
	a = []
	for i in str(n):
		a = [i]+a
	return "".join(a)
print(rev(5121))

def format_num(n):
	a = str(n)
	return a[:-3]+","+a[-3:]
print(format_num(100000))

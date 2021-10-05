def high_low(txt):
	a = txt.split(" ")
	return max(a) +" "+min(a)
print(high_low("1 2 -3 4 5"))

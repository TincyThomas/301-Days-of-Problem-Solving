def tuck_in(lst1, lst2):
	s = str(lst2)
	q = print("[", end = "")
	b = print(str(lst1[0]), end=",")
	a = print(s[1:-1],end=",")
	c = print(str(lst1[1]),end = "")
	w = print("]", end="")
	return ""
print(tuck_in([15,150], [45, 75, 35]))

def inator_inator(inv):
	a = len(inv)
	q = ["a","e","i","o","u"]
	if inv[-1] in q:
		return inv+"-inator "+ str(a) +"000"
	else:
		return inv+"inator " + str(a) + "000"
print(inator_inator("EvilClone"))

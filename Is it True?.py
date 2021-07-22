def is_it_true(relation):
	a = list(str(relation))
	if a[1]=="=":
		a[1]= "=="
	if eval("".join(a))== True:
		return True
	else:
		return False
print(is_it_true("7=7"))

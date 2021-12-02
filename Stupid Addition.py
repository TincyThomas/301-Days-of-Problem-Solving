def stupid_addition(a, b):
	if type(a) and type(b) == int:
		a = str(a)
		b = str(b)
		return a+b
	elif (type(a)==str and type(b)==int) or (type(a)==int and type(b)==str):
		return None
	else:
		a = int(a)
		b = int(b)
		return a+b
print(stupid_addition(1, 2))

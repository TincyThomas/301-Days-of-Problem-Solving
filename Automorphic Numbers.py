def is_automorphic(n):
	a = n**2
	b = str(a)
	if b[-1] == str(n):
		return True
	else:
		return False
print(is_automorphic(8))

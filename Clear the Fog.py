def clear_fog(txt):
	a = ""
	for i in txt:
		if i == "f" or i== "F"  or i == "o" or i == "O" or i == "g" or i == "G":
			pass
		else:
			a = a + i
	if a == txt:
		return "It's a clear day!"
	return a
print(clear_fog("fogfogFFfoooofftogffreogffesGgfOogfog"))

def superheroes(heroes):
	a = []
	for i in heroes:
		if i[-3:] == "man":
			if i[-5:].lower() == "woman":
				continue
			else:
				a = a + [i]
	return a
print(superheroes(["Wonder-Woman", "Catwoman", "Invisible-Woman"]))

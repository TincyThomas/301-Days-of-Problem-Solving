def remove_enemies(names, enemies):
	a = []
	for i in names:
		if i in enemies:
			continue
		else:
			a = a + [i]
	return a
print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]))

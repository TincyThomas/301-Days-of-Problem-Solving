def skip_the_sugar(drinks):
	a = []                                                        # empty list
	for d in drinks:                                              # looping drinks
		if d == "cola" or d == "fanta":                             # we do not want these two items
			continue
		else:
			a = a + [d]                                               # append rest
	return a
print(skip_the_sugar(["fanta", "cola", "water"]))

def get_fillings(sandwich):
	a = [sandwich[0]]+[sandwich[-1]]                                  # concatenating first and last elements
	b = []                                                            # assigning empty list
	for i in sandwich:                                                # looping elements of sandwich
		if i != a[0] or i!=a[-1]:                                       # we do not want first and last elements so do not include them
			b = b + [i]                                                   # add all other elements to empty list
	return b                                                          # finally return b
print(get_fillings(["bread", "lettuce", "bacon", "tomato", "bread"]))

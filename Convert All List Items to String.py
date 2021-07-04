def parse_list(lst):
	a = []                                        # dummy list
	for i in lst:                                 # looping elements of list
		a = a + [str(i)]                            # making each element string
	return a
print(parse_list([1, 2, "a", "b"]))

def get_multiplied_list(lst):
	a = []                                    # empty list
	for i in lst:                             # looping input list
		i = i *2                                # multiplying every input with 2
		a = a+[i]                               # appending after multiplication
	return a
print(get_multiplied_list([2, 5, 3]))

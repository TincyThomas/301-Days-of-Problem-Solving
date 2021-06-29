def invert_list(lst):
	a = list()                  # making input lst a string
	for i in lst:               # looping elements of list
		a = a + [-i]              # appending negative of looped element into a variable
	return a
print(invert_list([]))

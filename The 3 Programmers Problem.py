def programmers(one, two, three):
	list = [one,two,three]                      # making numbers in a list format for the ease of looping
	small = one                                 # assigning one to small
	for i in list:                              # looping elements of list
		if small >= i:                            # checking whether loop elements is equal to samll or less
			small= i                                # if there exists number smaller than small then make that number small
	big = one                                   # same as what happens with small
	for j in list:
		if ( big <= i):
			big =i
	return big - small
print(programmers(10, 5, 9))                  # Function calling and printing

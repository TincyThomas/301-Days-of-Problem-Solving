def rotate_by_one(lst):
	a =[]                                                         # dummy assignment
	b = lst[len(lst)-1]                                           # taking last element of lst to a new variable
	a = a + [b]                                                   # concatenating last element to dummy variable
	c = lst[0:len(lst) - 1]                                       # cutting first four elements out of original lst
	for i in range(1,len(lst)):                                   # looping from 1 to length of lst
		for j in c:                                                 # looping those first four elements
			a = a +[j]                                                # concatenating those four elements to dummy variable
		return a                                                    # atlast returning new dummy variable
print(rotate_by_one([20, 15, 26, 8, 4]))                        # Function calling and printing

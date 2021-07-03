def wumbo(words):
	q=""                                          # dummy list
	for i in words:                               # traversing elements of words
		if i == "M":                                # we have to change occurences of M only
			i="W"                                     # assign M to W
			q = q + i                                 # concatenation
		else:
			q = q + i
	return q
print(wumbo("MEET ME IN WARSAW"))

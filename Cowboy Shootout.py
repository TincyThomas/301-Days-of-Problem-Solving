def roger_shots(lst):
	count = 0                                   # initialization
	for i in lst:                               # looping through input
		if i == "Bang!" or i== "BangBang!":       # we want only two keywords
			count = count + 0.5                     # add 0.5 when we meet what we want
		else:
			continue                                # continue otherwise
	return count
print(roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!", "BangBang!"]))

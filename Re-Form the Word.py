def get_word(left, right):
	st = left+right                         # concatenate two input
	a= st[0]                                # take first char
	return a.upper()+st[1:len(st)+1]        # make first char uppercase then concatenate rest
print((get_word("lang", "uage")))

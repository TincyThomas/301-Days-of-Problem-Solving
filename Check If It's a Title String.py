def check_title(txt):
	a = txt.split(" ")                                          # splitting to list format with space
	for word in a:                                              # taking elements of a
		if (word[0][0].isupper()):                                # checking first element of every word is it upper case or not
			continue
		else: return False
	return True

print(check_title("A Mind boggling Achievement"))             # Function calling and printing

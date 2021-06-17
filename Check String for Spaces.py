def has_spaces(txt):
	for char in txt:                    # looping char in text
		if char ==" ":                    # check whether it is equal to space
			return True
	else: return False
print(has_spaces(",. /!@#"))          # Function calling and printing

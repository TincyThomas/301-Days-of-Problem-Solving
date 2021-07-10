def reverse_case(txt):
	a = ""                                            # assignment
	for char in txt:                                  # looping char of text
		if char == char.upper():                        # checking char equals its upper case
			a = a + char.lower()                          # make it lower case
		else:
			a = a+ char.upper()                           # make it upper case
	return a
print(reverse_case("Happy Birthday"))

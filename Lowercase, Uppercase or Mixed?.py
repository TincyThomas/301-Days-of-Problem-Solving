def get_case(txt):
	if txt.isupper():                       # checking whether it is in uppercase
		return "Upper"
	elif txt.islower():                     # checking whether it is in lowercase
		return "Lower"
	else:
		return "Mixed"                        # seems string is in mixedcase
print(get_case("whisper..."))

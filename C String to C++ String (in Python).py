def cpp_txt(lst):
	for i in lst:                             # looping list lst
		if i == "\0":                           # check where is "\0"
			lst[lst.index(i)]=""                  # make that index equal to ""
			return "".join(lst)                   # joining list into string format
print(cpp_txt(["H", "i", "!", "\0"]))

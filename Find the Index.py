def find_index(lst, txt):
	for i in lst:                                   # loop elements of list
		if i == txt:                                  # check element becomes equal to i
			return lst.index(txt)                       # print index of txt in list
print(find_index(["a", "g", "y", "d"], "d"))

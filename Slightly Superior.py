def is_first_superior(lst1, lst2):
	main = [lst1,lst2]                                                    # concatenating two lists to one
	for i in range(len(lst1)):                                            # looping to take value of i which is equivalent index of sub list
		if main[0][i] > main [1][i]:                                        # checking whether elements of first greater than second
			return True                                                       # if greater then return True
	else:
		return False                                                        # otheriwse return False
print(is_first_superior(["a", "zebra", "c"], ["a", "ant", "c"]))        # function calling

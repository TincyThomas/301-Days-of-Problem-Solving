def has_same_bread(lst1, lst2):
	l = [lst1]+[lst2]                                   # taking two lists into one
	for i in range(3):                                  # loop till 3
		if l[0][0] != l[1][0]:                            # checking first element's first and second element's first with equality 
			return False
		elif l[0][-1] != l[1][-1]:                        # checking first element's last and second element's last with equality 
			return False
		else:
			return True
print(has_same_bread(["white bread", "lettuce", "bread"],["white bread", "tomato", "white bread"]))

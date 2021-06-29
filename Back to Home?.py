def back_to_home(directions):
	d = list(directions)                      # converted string to list
	for i in d:                               # looping characters of directions
		if d.count(i) % 2 != 0:                 # I see a pattern, i.e. if the count of each direction is even then we land at same point
			return False
		else:
			return True


print(back_to_home("EWWE"))                 # Function calling and printing


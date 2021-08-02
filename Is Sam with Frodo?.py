def middle_earth(lst):
	count = -1
	for i in lst:
		count = count +1
		if i == "Sam":
			if lst[count-1] == "Frodo" or lst[count+1] == "Frodo":
				return True
		elif i == "Frodo":
			if lst[count+1] == "Sam" or lst[count-1] == "Sam":
				return True
		else:
			return False
print(middle_earth(["Sam", "Frodo"]))

def thirdthird(lst):
	for idx, i in enumerate(lst):
		if idx == 2:
			if len(i) >= 3:
				return i[2]
	return False
print(thirdthird(["BILL","GATES","ELON","MUSK"]))

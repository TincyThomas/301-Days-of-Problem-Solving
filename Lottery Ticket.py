def lottery(ticket, win):
	res = 0
	for j in ticket:
		for i in j[0]:
			if ord(i)==j[1]:
				res +=1
	return "Winner!" if res >= win else "Loser!"
print(lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1))

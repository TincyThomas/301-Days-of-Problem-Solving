def count(deck):
	a = 0
	for i in deck:
		if i == 2 or i == 3 or i== 4 or i== 5 or i== 6:
			a = a + 1
		elif i == 7 or i == 8 or i== 9:
			a = a + 0
		elif i == 10 or i== "J" or i== "Q" or i== "K" or i== "A":
			a = a - 1
	return a
print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))

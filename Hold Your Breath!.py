def diving_minigame(lst):
	a = 10
	for i in lst:
		if i < 0:
			a = a - 2
		else:
			a = a + 2
	return False if a ==0 else True
print(diving_minigame([-3, -6, -2, -6, -2]))

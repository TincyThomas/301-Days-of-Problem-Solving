def society_name(friends):
	a = ""
	for i in friends:
		a = a + i[0]
	return a.sort()
print(society_name(["Adam", "Sarah", "Malcolm"]))

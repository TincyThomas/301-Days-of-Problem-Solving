def mumbling(s):
	a = s[0]
	i = 1
	for j in s[1:]:
		a = a + "-" + (j.upper()) + (j.lower())*i
		i = i+1
	return a
print(mumbling("EdaBit"))

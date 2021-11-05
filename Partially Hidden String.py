def partially_hide(phrase):
	a = phrase.split(" ")
	print(a)
	c = ""
	count = -1
	for i in a:
		for j in i:
			count = count +1
			if count == 0 or count == len(i)-1:
				c = c + j
			else:
				c = c + "-"
		c = c + " "
		count = -1
	return c
print(partially_hide("skies were pretty"))

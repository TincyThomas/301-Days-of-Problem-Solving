def capital_letters(txt):
	count =0
	for i in txt:
		if i.isupper():
			count = count+1
	return count
print(capital_letters("mqeytbbjwqemcdrdsYvq"))

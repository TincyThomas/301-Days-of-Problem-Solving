def de_nest(lst):
	a = str(lst)
	b = ""
	for i in a:
		if i == "[" or i == "]":
			continue
		else:
			b = b + i
	return b
print(de_nest([[[[[[[True]]]]]]]))

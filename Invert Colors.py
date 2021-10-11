def color_invert(rgb):
	a = []
	for i in rgb:
		a = a + [255-i]
	return a
print(color_invert((255, 255, 255)))

def find_vertex(a, b, c):
	x = -b/(2*a)
	y = a*x*x + b*x + c
	return [int(x),int(y)]
print(find_vertex(1, 10, 4))

def find_vertex(a, b, c):
	v = -b/(2*a)
	return [round(v,2), round((a*((v)**2))+(b*v)+c,2)]
print(find_vertex(1, 10, 4))

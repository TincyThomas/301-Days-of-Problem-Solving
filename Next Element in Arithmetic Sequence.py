def next_element(lst):
	ele1 = lst[0]
	ele2 = lst[1]
	d = [ele1,ele2]
	d.sort()
	dif = d[1]-d[0]
	l  = lst[len(lst)-1]
	if l <0:
		return ((l*-1)+dif)*(-1)
	else:
		return (l + dif)
print(next_element([-5, -6, -7]))

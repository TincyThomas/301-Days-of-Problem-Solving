def next_in_line(lst, num):
	l = lst[1: len(lst)]
	l = l+[num]
	return l
print(next_in_line([5, 6, 7, 8, 9], 1))

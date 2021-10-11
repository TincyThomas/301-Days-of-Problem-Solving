def scale_tip(lst):
	a = lst[:int(len(lst)/2)]
	le = 0
	ri  = 0
	for i in a:
		le = le + i
	b = lst[int(len(lst)/2)+1:]
	for j in b:
		ri = ri + j
	if le == ri:
		return "balanced"
	return "right" if ri>le else "left"
print(scale_tip([1, 2, 3, "I", 1,2,3]))

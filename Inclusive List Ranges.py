def inclusive_list(start_num, end_num):
	a = [start_num]
	for i in range(start_num+1,end_num+1):
		a = a + [i]
	return a
print(inclusive_list(10, 15))

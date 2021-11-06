def number_len_sort(lst):
	p = 0
	count = -1
	while(p<len(lst)):
		for j in lst[:len(lst)-1]:
			count = count + 1
			if len(str(lst[count]))<=len(str(lst[count+1])):
				continue
			else:
				a = lst[count]
				lst[count] = lst[count+1]
				lst[count+1] = a
		count = -1
		p = p + 1
	return lst
print(number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]))
	

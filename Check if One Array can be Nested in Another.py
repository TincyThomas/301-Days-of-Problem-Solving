def can_nest(list1, list2):
	list1.sort()                                                                                # sorting first list
	list2.sort()                                                                                # sorting second list
	return True if list1[0]>list2[0] and list1[len(list1)-1]< list2[len(list2)-1] else False    # satisfying required conditions
print(can_nest([1, 2, 3, 4], [2, 3]))

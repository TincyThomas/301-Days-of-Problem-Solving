def modify_last(txt, n):
	return txt[:] + txt[len(txt)-1]*(n-1)         # return all elements as it is except last, concatenate with last n times
print(modify_last("What?", 3))

def index_shuffle(txt):
	even = ''
	odd = ''
	for i in range(0,len(txt),2):
		even = even + txt[i]
	for j in range(1,len(txt),2):
		odd = odd + txt[j]
	return even+odd
print(index_shuffle("abcd"))

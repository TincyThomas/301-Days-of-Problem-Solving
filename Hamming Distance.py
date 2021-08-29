def hamming_distance(txt1, txt2):
	count = 0
	for i in range(len(txt1)):
		if txt1[i] != txt2[i]:
			count = count+1
	return count
print(hamming_distance("strong", "strung"))

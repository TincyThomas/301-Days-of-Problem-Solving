def find_letters(word):
	a = []                          # empty list                    
	for i in word:                  # looping through input word
		if word.count(i) == 1:        # count every character
			a = a + [i]                 # print those whose count is one
	return a
print(find_letters("analysis"))

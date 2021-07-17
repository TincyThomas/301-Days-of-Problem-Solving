'''
def sort_word(word):
	word = word.split('')
	word = list(word.sort())
	final_word = ''
	
	for char in word
		final_word = final_word + char
	
	return final_word
'''


def sort_word(word):

    if word[0] == word[0].isupper():                  # checking first letter to be uppercase
        w = list(word[1:])                            # making list of all char except first
        w.sort()                                      # sort list
        return word[0] + "".join()
    else:
        w = list(word)
        w.sort()
        return "".join(w)

print(sort_word("Disney"))

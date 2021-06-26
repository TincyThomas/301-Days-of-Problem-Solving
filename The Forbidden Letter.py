def forbidden_letter(char, lst):
	for word in lst:                                                                  # looping through words in list
		for chara in word:                                                              # looping through characters in words
			return False if char == chara else True                                       # returns true when the letter does not appear in any of the words.
print(forbidden_letter("b", ["rock", "paper", "scissors"]))

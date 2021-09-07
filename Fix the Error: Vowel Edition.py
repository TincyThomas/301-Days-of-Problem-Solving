# Fix this incorrect code, so that all tests pass!
"""def remove_vowels(string):
	vowels = "aeiou"
    for vowel in vowels[1]:
    	string.replace(vowel, "", 1)
    return string""""
		
# Fixed codde below
def remove_vowels(string):
    vowels = "aeiou"
    for vowel in vowels[1]:
        a = string.replace(vowel, "",1)
    return a
print(remove_vowels("ben"))

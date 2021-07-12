str1 = "abcdefghijklmnopqrstuvwxyz"
str2 = "abcdefghijklmnopqrstuvwxyz"
def longest_string(str1, str2):
	a = str1+str2
	a = set(a)
	a = sorted(a)
	a="".join(a)
	return print(a)
longest_string(str1,str2)

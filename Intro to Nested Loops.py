def print_all_groups():
	import string
	alphabet_string = string.ascii_lowercase
	alphabet_list = list(alphabet_string)
	aw = alphabet_list[0:5]
	qa = ""
	for i in range(1,7):
		for j in aw:
			qa = qa + (str(i)+j+" ")
	return qa
print(print_all_groups())

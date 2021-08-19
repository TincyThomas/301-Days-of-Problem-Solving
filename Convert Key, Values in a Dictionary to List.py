def dict_to_list(d):
	a = []
	for k, v in d.items():
		a = a +[tuple([k,v])]
	return a
print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}))

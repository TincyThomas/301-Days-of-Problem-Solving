def count_towers(towers):
	a = ""
	for i in towers[-1]:
		a = a + i
	return a.count("##")
print(count_towers([
  ["     ##         "],
  ["##   ##        ##"],
  ["##   ##   ##   ##"],
  ["##   ##   ##   ##"]
]))

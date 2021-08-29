def count_characters(lst):
	count = 0
	for i in lst:
		for j in lst:
			count = count + 1
	return count
print(count_characters([
  "###",
  "###",
  "###"
]))

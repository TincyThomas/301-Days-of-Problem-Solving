def count_ones(matrix):
	count = 0
	for i in matrix:
		for j in i:
			if j == 1:
				count = count+1
	return count
print(count_ones([
  [1, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]))

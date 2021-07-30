def calc_determinant(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][1]
print(calc_determinant([
  [1, 1],
  [1, 1]
]))

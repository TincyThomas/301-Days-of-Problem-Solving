def convert(data1, data2):
  a = type(data1)
  for i in data2:
    if a == tuple:
      return tuple(data2)
    elif a == list:
      return list(data2)
    if a == set:
      return set(data2)
  return a
print(convert((7, 8, 9), [1, 2, 4, 8]))

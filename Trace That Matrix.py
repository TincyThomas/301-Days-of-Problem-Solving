def trace(lst):
    a = 0
    q = 0
    for i in lst:
        q = q + i[a]
        a = a + 1
        continue
    return q
print(trace([
  [1, 0, 1, 0],
  [0, 2, 0, 2],
  [3, 0, 3, 0],
  [0, 4, 0, 4]
]))

def sum_of_evens(lst):
    a = 0
    for i in lst:
        for j in i:
            if j % 2 ==0:
                a = a +j
    return a
print(sum_of_evens([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]))

def minimum_removals(lst):
    a = 0
    for i in lst:
        a = a + i
    if a%2==0:
        return 0
    else:
        return 1
print(minimum_removals([5, 7, 9, 12]))

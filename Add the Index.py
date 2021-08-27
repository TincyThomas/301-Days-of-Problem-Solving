def add_indexes(lst):
    count = -1
    a = []
    for i in lst:
        count = count + 1
        a = a + [i + count]
    return a


print(add_indexes([1, 2, 3, 4, 5]))

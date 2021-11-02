def ranged_reversal(lst, start, finish):
    count = -1
    a = []
    for i in lst:
        count = count+1
        if count == start:
            a = a + [lst[finish]]
            continue
        if count == finish:
            a = a + [lst[start]]
        else:
            a = a + [i]
    return a
print(ranged_reversal([1, 2, 3, 4, 5, 6], 0, 4))

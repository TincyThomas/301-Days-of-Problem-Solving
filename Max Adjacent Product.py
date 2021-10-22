def adjacent_product(lst):
    a = []
    for i in range(1,len(lst)):
        a = a + [lst[i]*lst[i-1]]
    return max(a)
print(adjacent_product([3, 6, -2, -5, 7, 3] ))

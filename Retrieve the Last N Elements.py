def last(a, n):
    q = []
    for i in range(-1, -(n+1), -1):
        q = [a[i]] + q
    return q

print(last([1, 2, 3, 4, 5], 3))

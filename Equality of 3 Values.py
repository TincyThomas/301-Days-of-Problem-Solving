def equal(a, b, c):
    q = [a,b,c]
    w = []
    for i in q:
        w = w + [q.count(i)]
    if max(w) == 1:
        return 0
    else:
        return max(w)
print(equal(2, 2, 3))

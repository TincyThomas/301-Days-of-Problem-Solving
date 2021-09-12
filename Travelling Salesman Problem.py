def paths(n):
    a = 1
    for i in range(n,1,-1):
        a = a*i
    return a
print(paths(4))

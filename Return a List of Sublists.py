def matrix(x, y, z):
    a = []
    q = []
    for i in range(x):
        for j in range(y):
            a = a + [z]
        q =q + [a]
        a = []
    return q
print(matrix(2, 1, "edabit"))

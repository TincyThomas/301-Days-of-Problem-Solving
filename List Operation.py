def list_operation(x, y, n):
    a = []
    for i in range(x,y+1):
        if i%3 == 0:
            a = a + [i]
    return a
print(list_operation(1, 10, 3))

def marathon_distance(d):
    a = 0
    for i in d:
        if i < 0:
            i = str(i)
            a = a + int(i[1:])
        else:
            a = a + i
    return True if a == 25 else False
print(marathon_distance([1, 2, 3, -4]))

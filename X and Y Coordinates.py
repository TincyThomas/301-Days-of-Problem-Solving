def convert_cartesian(x, y):
    a = []
    count = -1
    for i in range(len(x)):
        count = count + 1
        a = a + [[x[count],y[count]]]
    return a
print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) )

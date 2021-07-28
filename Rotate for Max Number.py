def rotate_max_number(num):
    a = []
    w=""
    s = list(str(num))
    for i in s:
        a = a + [int(i)]
    a.sort(reverse=1)
    for j in a:
        w = w+str(j)
    return w
print(rotate_max_number("001"))

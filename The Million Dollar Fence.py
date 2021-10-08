def construct_fence(p):
    a = ""
    for i in p:
        if i.isdigit():
            a = a + i
    ab = str(a)
    pr = int(1000000/int(ab))
    return pr *'H'
print(construct_fence("$100,000"))

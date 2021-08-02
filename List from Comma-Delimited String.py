def to_array(txt):
    count = 0
    start = 0

    a = []
    for i in txt:
        count = count +1
        if i == ",":
            a = a + [txt[start:(count-1)]]
            start = count + 1
    else:
        a = a+[txt[start:len(txt)]]
    return a
print(to_array("a, b, c, d"))

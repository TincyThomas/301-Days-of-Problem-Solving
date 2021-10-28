def partition(txt, n):
    t = []
    for i in range(0,len(txt),n):
        t = t + [txt[i:i+n]]

    return t
print(partition("thematic", 4))

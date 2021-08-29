def move_to_end(lst, el):
    a = []
    for i in lst:
        if i != el:
            a = a+[i]
    b = lst.count(el)
    for i in range(b):
        a = a + [el]
    return a
print(move_to_end([1, 3, 2, 4, 4, 1], 2))

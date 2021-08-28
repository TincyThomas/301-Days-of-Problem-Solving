def filter_list(lst):
    a = []
    for i in lst:
        if type(i) == int:
            a = a+[i]
    return a
print(filter_list([1, 2, "a", "b"]))

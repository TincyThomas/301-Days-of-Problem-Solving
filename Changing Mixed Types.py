def change_types(lst):
    a = []
    for i in lst:
        if type(i) == int:
            if i%2==0:
                a = a + [i + 1]
            else:
                a = a + [i]
        elif type(i) == str:
            a = a + [i[0].upper() + i[1:].lower() + "!"]
        elif type(i) == bool:
            a = a + [not(i)]
    return a
print(change_types(["a", 12, True]))

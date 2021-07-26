def add_ending(lst, ending):
    a = []
    for i in lst:
        a= a + [i+ending]
    return a
print(add_ending(["new", "pander", "scoop"], "er"))

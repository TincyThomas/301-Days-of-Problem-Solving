def spelling(txt):
    a = []
    for i in range(1,len(txt)+1):
            a = a +[txt[:i]]
    return a
print(spelling("bee"))

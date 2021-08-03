def mirror(lst):
    a = lst
    b =[]

    for i in lst[0:(len(lst) - 1)]:
        b = [i] + b
    return a+b
print(mirror([0, 2, 4, 6]))

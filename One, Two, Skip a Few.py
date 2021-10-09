def how_many_missing(lst):
    min = lst[0]
    max = lst[-1]
    num = (max-min)-1
    a = len(lst)-2
    return num - a
print(how_many_missing([1, 3, 5, 7, 9, 11]))

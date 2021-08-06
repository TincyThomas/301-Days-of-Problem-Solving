def filter_unique(lst):
    a = []
    for i in lst:
        if len(set(i)) == len(i):
            a = a +[i]
    return a
print(filter_unique(["abb", "mike","abc", "abcdb", "aea", "bbb"]) )

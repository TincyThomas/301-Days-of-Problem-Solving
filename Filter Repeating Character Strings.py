def identical_filter(lst):
    a  = []
    for i in lst:
        b=set(i)
        if len(b)==1:
            a = a+[i]
    return a
print(identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"]))

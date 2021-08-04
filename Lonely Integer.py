def lonely_integer(lst):
    for i in lst:
        if -i not in lst:
            return i

print(lonely_integer([-9, -105, -9, -9, -9, -9, 105]))

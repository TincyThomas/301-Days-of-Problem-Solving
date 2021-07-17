def negate(lst):
    a = []                    # empty list
    for i in lst:             # looping input
        i = i*(-1)            # multiplying every element with -1 to get negate output
        a = a + [i]           # appending to list
    return a
print(negate([-1, 2, -3, 4]))

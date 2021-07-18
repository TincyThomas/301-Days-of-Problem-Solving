def additive_inverse(lst):
    a = []                                      # empty list
    for i in lst:                               # looping input lst
        a = a + [i*-1]                          # appending to list,  negate values
    return a
print(additive_inverse([5, -7, 8, 3]))

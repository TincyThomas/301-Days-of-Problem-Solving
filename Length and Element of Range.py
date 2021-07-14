def length_element(r, i):
    a = []                                  # empty list
    for k in r:                             # looping through given range
        a = a + [k]                         # list of given range elements
    return [len(a),a[i]]                    # return a list of length and element at given index
print(length_element(range(12, 15, 2), 1))

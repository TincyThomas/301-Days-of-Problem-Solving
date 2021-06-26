def first_last(lst):
    a = []
    for i in lst:                                 # looping elements of lst
        if lst.index(i) == 0:                     # taking first element
            a = a+[i]
        elif lst.index(i) == len(lst)-1:          # taking last element
            a = a + [i]
    return a                                      # returning first and last elements in a list

print(first_last(["no", 10, 15, 20, 25]))         # Function calling and printing

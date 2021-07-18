def add_up_to(n):
    a = []                          # empty list
    sum = 0                         # initialization
    for i in range(n+1):            # looping through given input range
        a = a + [i]                 # printing every looping element
    for j in a:                     # looping newly created list
        sum = sum + j               # adding all elements of list
    return sum
print(add_up_to(7))

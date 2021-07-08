def find_difference(a, b):
    q=1                                           # dummy assignment
    w=1                                           # initialisation
    for i in a:                                   # looping elements of a
        q = q*i                                   # multiplying each of i with previous
    for j in b:                                   # looping elements of b
        w =w*j                                    # multiplying each of j with previous
    if q-w < 0:                                   # if number is negative 
        return (q-w)*(-1)                         # multiplying by -1 gives positive number
    else:
        return q-w                                # print number
print(find_difference([2, 2, 3], [5, 4, 1]))

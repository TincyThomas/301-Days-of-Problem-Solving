def trimmed_averages(lst):
    lst.sort()                              # sorting list
    b = lst[1:len(lst)-1]                   # taking list excluding greatest and smallest
    q=0                                     # initialization
    for i in b:                             # looping in new list
        q = q+i                             # adding every elements
    return int(q/len(b))                    # dividing by length to get average
print(trimmed_averages([4, 5, 7, 100]))

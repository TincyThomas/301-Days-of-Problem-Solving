def remove_smallest(lst):
    m = min(lst)
    index = lst.index(m)
    nm = lst[0:index]
    mn =  lst[index+1:len(lst)]
    return nm +mn
print(remove_smallest([5, 3, 2, 1, 4]))

def median(lst):
    lst.sort()
    if len(lst)%2==0:
        return (lst[int(len(lst)/2)]+ lst[int(len(lst)/-2)])/2
    else:
        return lst[int(len(lst)/2)]
print(median([2, 5, 6, 2, 6, 3, 4]))

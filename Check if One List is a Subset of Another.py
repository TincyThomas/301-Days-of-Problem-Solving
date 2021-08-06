def subset(lst1, lst2):
    a = set(lst1)
    count =0
    for i in a:
        if i in lst2:
            count = count+1
            if count == len(a):
                return True
    else:
        return False
print(subset([1, 3,2], [1, 3, 3, 5]))

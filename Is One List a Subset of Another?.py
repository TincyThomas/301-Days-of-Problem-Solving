def is_subset(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    else:
        return True
print(is_subset([3, 2, 77], [5, 3, 7, 9, 2]))

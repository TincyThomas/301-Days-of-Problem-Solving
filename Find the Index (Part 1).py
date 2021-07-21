def search(lst, item):
    count = 0
    for ite in lst:
        count = count + 1
        if ite == item:
            return count
    else:
        return -1
print(search([1, 2, 4], 4))

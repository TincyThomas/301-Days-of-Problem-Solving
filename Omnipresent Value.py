def is_omnipresent(lst, val):
    count = 0
    for i in lst:
        if val in i:
            count = count +1
            if len(lst)==count:
                return True
        else:
            return False
print(is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 7))

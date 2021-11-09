def is_special_array(lst):
    count = -1
    for i in lst:
        count = count + 1
        if count % 2 == 0:
            if i % 2 == 0:
                continue
            else:
                return False
        else:
            if i % 2 != 0:
                continue
            else:
                return False
    return True

print(is_special_array([2, 7, 9, 1, 6, 1, 6, 3]))


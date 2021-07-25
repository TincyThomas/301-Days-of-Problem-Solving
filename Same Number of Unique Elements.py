def same(a1, a2):
    a = set(a1)
    b = set(a2)
    if len(a) == len(b):
        return True
    else:
        return False


print(same([1,6,3, 4, 4, 4], [2, 5, 7]))

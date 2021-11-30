def lines_are_parallel(l1, l2):
    return True if (-(l1[0]) / l1[1]) == (-(l2[0]) / l2[1]) else False


print(lines_are_parallel([2, 4, 1], [2, 4, 1]))

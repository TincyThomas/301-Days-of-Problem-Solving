def upward_trend(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] < lst[i]:
            continue
        else:
            return False
    else:
        return True


print(upward_trend([1, 2, 6, 7, 8]))

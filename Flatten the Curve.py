def flatten_the_curve(lst):
    summ = 0
    for i in lst:
        summ = summ + i
    a = int(summ / len(lst))
    return [a for i in range(len(lst))]


print(flatten_the_curve([0, 0, 0, 2, 7, 3]))

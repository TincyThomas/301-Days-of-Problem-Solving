def outlier_number(lst):
    counteven = 0
    countodd = 0
    for i in lst:
        if i % 2 == 0:
            counteven = counteven + 1
        else:
            countodd = countodd + 1
    if counteven < countodd:
        for j in lst:
            if j % 2 == 0:
                return j
    else:
        for j in lst:
            if j % 2 != 0:
                return j


print(outlier_number([2, 5, 7]))

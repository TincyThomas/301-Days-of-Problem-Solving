def sum_minimums(lst):
    a = 0                       # initial assignment
    for lis in lst:             # looping every rows
        a = a + lis[0]          # taking first element of every row
    return a                    # return total sum of all 0th element


print(sum_minimums([
    [1, 2, 3, 4, 5],
    [2, 6, 7, 8, 9],
    [15, 21, 34, 56, 100]
]))

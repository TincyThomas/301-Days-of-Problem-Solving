def sum_first_n_nums(lst, n):
    sum = 0                           # initialization
    for i in lst:                     # looping input list
        if i == lst[n-1]:             # untill required index
            sum = sum + i             # final add
            break
        else:
            sum = sum + i             # keep adding
    return sum


print(sum_first_n_nums([1, 3, 2], 2))

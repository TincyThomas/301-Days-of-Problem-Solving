def odd_sum_list(lst):
    a = []
    for i in range(0,len(lst)-1):
        if (lst[i]+lst[i+1]) %2 ==0:
            a= a+["True"]
        else:
            a = a+["False"]
    return a
print(odd_sum_list([11, 15, 6, 8, 9, 10]))

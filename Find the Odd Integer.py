def find_odd(lst):
    for i in lst:
        #print(i,lst.count(i))
        if lst.count(i) %2 !=0:
            return i
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))

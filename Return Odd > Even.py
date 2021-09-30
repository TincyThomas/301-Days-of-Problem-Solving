def oddeven(lst):
    counto=0
    counte=0
    for i in lst:
        if i %2==0:
            counte = counte+1
        else:
            counto=counto+1
    return True if counto>counte else False
print(oddeven([13452394823795273847528572346]))

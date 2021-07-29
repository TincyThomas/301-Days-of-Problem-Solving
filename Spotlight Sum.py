def spotlight_sum(n):
    b = 0
    a = [n, n+1,n-1,n-10,n-10-1,n-10+1,n+10,n+10+1,n+10-1]
    for i in a:
        b = b+i
    return b
print(spotlight_sum(45))

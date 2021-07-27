def number_squares(n):
    a = 0
    for i in range(n+1):
        a = a+ (i*i)
    return a
print(number_squares(5))

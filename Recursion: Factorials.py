def factorial(n):
    a = 1
    for i in range(2,n+1):
        a = a*i
    return a
print(factorial(3))

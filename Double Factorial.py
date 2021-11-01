def double_factorial(num):
    a = 1
    if num%2==0:
        for i in range(2,num+1,2):
            a = a * i
        return a
    else:
        for i in range(1,num+1,2):
            a = a * i
        return a
print(double_factorial(9))

def is_narcissistic(n):
    a = len(str(n))
    b = 0
    for i in str(n):
        b = b +int(i)**a
    return True if b == n else False
print(is_narcissistic(154))

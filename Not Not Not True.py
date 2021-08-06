def not_not_not(n, b):
    if b == True:
        return True if n%2==0 else False
    elif b == False:
        return False if n % 2 == 0 else True
print(not_not_not(6, True))

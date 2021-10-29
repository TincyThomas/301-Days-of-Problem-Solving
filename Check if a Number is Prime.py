def is_prime(num):
    a = []
    if num ==2:
        return True
    elif num>2 and num%2==0:
        return False
    else:
        for i in range(3,int(num/2)+1):
            a = a + [i]
            if num%i==0:
                return False
            else: continue
        return True
print(is_prime(9))

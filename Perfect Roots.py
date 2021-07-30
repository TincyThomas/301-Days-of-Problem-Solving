def perfect_roots(n):
    a = n**(1/2)
    b = n**(1/4)
    c = n**(1/8)
    if int(a) == a and  int(b)== b and int(c) == c:
        return True
    else:
        return False
print(perfect_roots(1000))

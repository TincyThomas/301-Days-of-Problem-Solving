def is_symmetrical(num):
    a = []
    b = []
    c = str(num)
    if len(c)%2==0:
        for i in range(0,int(len(c)/2)):
            a = a + [c[i]]
        #print("a",a)
        for j in range(len(c)-1,(int(len(c)/2)-1),-1):
            b = b + [c[j]]
        #print("b",b)
        if a == b:
            return True
        else:
            return False
    else:
        for i in range(0, int(len(c) / 2)):
            a = a + [c[i]]
        #print("a", a)
        for j in range(len(c) - 1, (int(len(c) / 2)), -1):
            b = b + [c[j]]
        #print("b", b)
        if a == b:
            return True
        else:
            return False
print(is_symmetrical(7257))
